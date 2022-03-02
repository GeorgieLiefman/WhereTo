from flask import Blueprint

auth = Blueprint("views", __name__)

@auth.route("/login")
def login():
    return "Login"

@auth.route("/sign_up")
def sign_up():
    return "Sign up"

@auth.route("/log_out")
def log_out():
    return "Log out"