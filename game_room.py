from flask import Blueprint, session, redirect, url_for, render_template

room = Blueprint(__name__, "room")


@room.route("/")
def home_room():
    if not session["host"]:
        # return render_template()
        return "test host"
    else:


        return f"This is game home page {session.get('game_code')}"

