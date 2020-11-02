from flask_ngrok import run_with_ngrok
from flask import Flask, redirect, url_for, render_template, request
from werkzeug.exceptions import BadRequestKeyError

from play_service import playService
from random import choice
import os
app = Flask(__name__)

myplay = playService()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/playUsingChoice', methods=["GET", "POST"])
def play():
    if request.method == "POST":
        if request.form['submit'] == 'rock':
            userchoice = 'rock'
        elif request.form['submit'] == 'scissors':
            userchoice = 'scissors'
        elif request.form['submit'] == 'paper':
            userchoice = 'paper'

    computerChoice = myplay.riggedchoice(userchoice, 80, 5)
    winner, computerscore, playerscore = myplay.decideWinner(userchoice,computerChoice)

    return render_template("result.html", valueplayerchoice=userchoice, valuecompchoice=computerChoice,
                           valuecompscore=computerscore, valueplayerscore=playerscore, valuewinner=winner)






#port = int(os.getenv("PORT"))
if __name__ == "__main__":

    app.run(host='127.0.0.1', port=8001, debug=True)
    #app.run(host='0.0.0.0', port=port)