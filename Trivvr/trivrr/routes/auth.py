from trivrr.extensions import db
from trivrr.models import User
from flask_login import login_user, logout_user
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        unhashed_password = request.form["password"]

        matched_users = User.query\
            .filter_by(name=name)\
            .all()

        user = User(
            name=name,
            unhashed_password=unhashed_password,
            points=0
        )
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        user = User.query.filter_by(name=name).first()
        
        login_user(user)
        return redirect(url_for("main.index"))
        
    return render_template("login.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))