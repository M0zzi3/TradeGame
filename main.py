from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

from datetime import timedelta
from user import User
from host import Host
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes = 60)
app.secret_key = "SuperUltraTajneNaPrawdeToTajneBardzo"
socketio = SocketIO(app)

GAMES = {}

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in GAMES:
            break
    return code

@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        if not name:
            return render_template("home.html", error="Please enter a name.", code=code, name=name)
        room = code
        
        if code not in GAMES:
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
        
        session["room"] = room
        session["name"] = name
        session["host"] = False
        return redirect(url_for("room"))

    return render_template("home.html")

@app.route("/host")
def hostGame():
    room = generate_unique_code(4)
    GAMES[room] = {"master":"", "members": 0, "canJoin":True, "usersObj":{}} 
    session["room"] = room
    session["host"] = True
    print("room Created")
    return render_template("host.html", code=room)

@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in GAMES or GAMES[room]["canJoin"] == False:
        return redirect(url_for("home"))
    return render_template("user.html", code=room)


@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name",   False)
    host = session.get("host")

    if not room or not name and host == False :
        return
    
    if room not in GAMES:
        leave_room(room)
        return
    
    join_room(room)
    if session.get("host"):
        master = Host(request.sid)
        GAMES[room]["master"] = master # type: ignore (someting wrong?)
        
    if not host:
        userObj = User(request.sid)
        GAMES[room]["usersObj"][request.sid] = userObj
        # print()
        socketio.emit("addUser", {"name": name}, to=GAMES[room]["master"].idd)
    GAMES[room]["members"] += 1
    print(f"{name} joined room {room}")

@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in GAMES:
        GAMES[room]["members"] -= 1
        if GAMES[room]["members"] <= 0:
            del GAMES[room]
    socketio.emit("deleteUser", {"name": name}, to=GAMES[room]["master"].idd)
    print(f"{name} has left the room {room}")


@socketio.on("periodEnd")
def updateAllVauleInGame():
    print("[UPDATE DATA]")
    room = session.get("room")
    masterObj = GAMES[room]["master"]
    masterObj.updatePeriod()
    daysleft = masterObj.days
    if masterObj.days <= 0:
        print("game End")
        socketio.emit("endGame", to=room)
    else:
        socketio.emit("updateValue", {"gold":masterObj.goldInGame.value}, to=room)
        socketio.emit("updateGameDays",{"daysleft":daysleft}, to=masterObj.idd)

@socketio.on("startGame")
def startGame(data):
    print("[StartGame]", data["setings"])
    room = session.get("room")
    if room not in GAMES:
        return 
    GAMES[room]["CanJoin"] = False
    GAMES[room]["master"].startGame()
    moneyOnStart = 100000
    for userIdd in GAMES[room]["usersObj"]:
        GAMES[room]["usersObj"][userIdd].setsettings(moneyOnStart)
    content = {"action":"STARTGAME"}
    socketio.emit("userStartGame", {"moneyOnStart":moneyOnStart}, to=room)
    updateAllVauleInGame()
    
@socketio.on("buy")
def buy(data):
    room = session.get("room")
    userObj = GAMES[room]["usersObj"][request.sid]
    masterObj = GAMES[room]["master"]
    print(data["whatBuy"])
    if userObj.money >= masterObj.goldInGame.value:
        userObj.money -= masterObj.goldInGame.value
        masterObj.goldInGame.buyUpdate()
        userObj.walletContents["gold"] += 1
    if room not in GAMES:
        return
    
    socketio.emit("updateWallet", {"transactionStatus":True, "money":userObj.money, "wallet":userObj.walletContents}, to=userObj.idd)

@socketio.on("sell")
def sell(data):
    room = session.get("room")
    userObj = GAMES[room]["usersObj"][request.sid]
    masterObj = GAMES[room]["master"]
    print(data["whatSell"])
    if userObj.walletContents["gold"] > 0:
        userObj.money += masterObj.goldInGame.value
        masterObj.goldInGame.sellUpdate()
        userObj.walletContents["gold"] -= 1
    if room not in GAMES:
        return
    
    socketio.emit("updateWallet", {"transactionStatus":True, "money":userObj.money, "wallet":userObj.walletContents}, to=userObj.idd)

if __name__ == "__main__":
    socketio.run(app, debug=True)
    # app.run(host="192.168.0.165",port = 80, debug=False) 