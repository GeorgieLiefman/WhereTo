from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Review, User, Comment
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


@views.route("/delete_review/<id>", methods=["GET"])
@login_required
def delete_review(id):
    review = Review.query.filter_by(id=id).first()

    if not review:
        flash("Review does not exist.", category="error")
    elif current_user.id != review.id:
        flash("You do not have permission to delete this post.", category="error")
    else:
        db.session.delete(review)
        db.session.commit()
        flash("Review deleted.", category="success")

    return redirect(url_for("views.home"))

@views.route("/reviews/<username>", methods=["GET"])
@login_required
def reviews(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No user with that username exists.", category="error")
        return redirect(url_for("views.home"))

    reviews = Review.query.filter_by(author=user.id).all()
    return render_template("reviews.html", user=current_user, reviews=reviews, username=username)


@views.route("/create_comment/<review_id>", methods=["POST"])
@login_required
def create_comment(review_id):
    text = request.form.get("text")
    if not text:
        flash("Comment cannot be empty.", category="error")
    else:
        review = Review.query.filter_by(id=review_id)
        if review:
            comment = Comment(text=text, author=current_user.id, review_id=review_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash("Review does not exist.", category="error")


    return redirect(url_for("views.home"))


@views.route("/delete_comment/<comment_id>", methods=["GET"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash("Comment does not exist.", category="error")
    elif current_user.id != comment.author and current_user.id != comment.review.author:
        flash("You do not have permission to delete this comment.", category="error")
    else:
        db.session.delete(comment)
        db.session.commit()
        

    return redirect(url_for("views.home"))