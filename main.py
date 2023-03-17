from flask import Flask, render_template, session, request
from gameHost import Host
from gamePlayer import Player
from datetime import timedelta


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes = 60)
app.secret_key = "SuperUltraTajneNaPrawdeToTajneBardzo"


AVAILABLE_GAME = {}

@app.route('/')
def home_page():  
    return render_template("home.html")

@app.route('/hostgame')
def host_game():
    game = Host()
    print("[SYSTEM] GAME CREATED ID: ", game.id) 
    AVAILABLE_GAME.update({str(game.id):game})
    return str(game.id) # Tutaj już rozpocząć web socketa 

@app.route('/playgame', methods=["POST","GET"])
def join_game():
    if request.method == "POST":
        userIdGameInput = request.form["gameid"]
        player = Player(AVAILABLE_GAME[userIdGameInput]) #! Sprawdzanie czy jest inne od zera w sensie czy tam rzeczywiście jest jakieś id 
        return "work"
        # return render_template("joingame.html") #? instancje player trzeba już wrzucić do sockta 

    else:
        return render_template("joingame.html")



if __name__ == '__main__':
    app.run()
