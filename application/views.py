from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Review
from . import db

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    reviews = Review.query.all()
    return render_template("home.html", name=current_user.username, user=current_user, reviews=reviews)


@views.route("/create_review", methods=["GET", "POST"])
@login_required
def create_review():
    if request.method == "POST":
        text = request.form.get("text")

        if not text:
            flash("Review cannot be empty", category="error")
        else:
            review = Review(text=text, author=current_user.id)
            db.session.add(review)
            db.session.commit()
            flash("Review created!", category="successful")
            return redirect(url_for("views.home"))

    return render_template("create_review.html", user=current_user)