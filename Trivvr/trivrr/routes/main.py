from flask import Blueprint, render_template, Flask 

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/page_one")
def page_one():
    return render_template("page_one.html")

@main.route("/page_two")
def page_two():
    return render_template("page_two.html")