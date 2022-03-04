from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    username = request.form.get("username")
    print(username)
    return render_template("signup.html")

@auth.route("/log_out", methods=["GET"])
def log_out():
    return redirect(url_for("views.home"))