from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

from datetime import timedelta

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
    GAMES[room] = {"master":"", "members": 0,"canJoin":True} 
    session["room"] = room
    session["host"] = True
    print("room Created")
    return render_template("host.html",code=room)

@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room not in GAMES or GAMES[room]["canJoin"] == False:
        return redirect(url_for("home"))
    return render_template("user.html", code=room)


@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name",False)
    host = session.get("host")

    if not room or not name and host == False :
        return
    
    if room not in GAMES:
        leave_room(room)
        return
    
    join_room(room)
    if session.get("host"):
        GAMES[room]["master"] = request.sid # type: ignore (someting wrong?)
        
    if not host:
        socketio.emit("addUser",{"name": name}, to=GAMES[room]["master"])
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
    socketio.emit("deleteUser",{"name": name}, to=GAMES[room]["master"])
    print(f"{name} has left the room {room}")


@socketio.on("periodEnd")
def updateAllVauleInGame():
    print("update data")
    room = session.get("room")
    
    socketio.emit("updateValue",{"gold":random.randint(0, 100)},to=room)

@socketio.on("startGame")
def message(data):
    print("[StartGame]")
    room = session.get("room")
    if room not in GAMES:
        return 
    GAMES[room]["CanJoin"] = False

    content = {"action":"STARTGAME"}
    # updateAllVauleInGame()
    send(content, to=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)