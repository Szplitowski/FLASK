from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/mypage/me")
def grit():
    return render_template("o_mnie.html")


@app.route("/mypage/contact", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        print("We received POST")
        print(request.get_data())
        return "Dziękuję za wiadomość!"
    elif request.method == "GET":
        print("We received GET")
        return render_template("kontakt.html")
