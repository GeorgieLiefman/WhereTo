from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    return render_template("home.html", name=current_user.username, user=current_user)


@views.route("/create_review", methods=["GET", "POST"])
@login_required
def create_review():
    return render_template("create_review.html", user=current_user)