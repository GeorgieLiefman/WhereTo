from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Review, User, Comment, Like
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
        title = request.form.get("title")
        content = request.form.get("content")
        destination = request.form.get("destination")
        category = request.form.get("category")
        price = request.form.get("price")

        if not title:
            flash("A review cannot be created without a title.", category="error")
        elif not content:
            flash("The content of a review cannot be empty.", category="error")
        elif not destination:
            flash("A destination needs to be entered to create a review.", category="error")
        elif not category:
            flash("Reviews cannot be created without the category of review being specified.", category="error")
        elif not price:
            flash("Reviews cannot be created without the price of review being specified. If the experience was free please specify so.", category="error")
        else:
            review = Review(title=title, content=content, destination=destination, category=category, price=price, creator=current_user.id)
            db.session.add(review)
            db.session.commit()
            flash("Review successfully created!", category="successful")
            return redirect(url_for("views.home"))

    return render_template("create_review.html", user=current_user)


@views.route("/delete_review/<id>", methods=["GET"])
@login_required
def delete_review(id):
    review = Review.query.filter_by(id=id).first()

    if not review:
        flash("The review you are trying to delete does not exist.", category="error")
    else:
        db.session.delete(review)
        db.session.commit()
        flash("The review has been successfully deleted.", category="success")

    return redirect(url_for("views.home"))


@views.route("/reviews/<username>", methods=["GET"])
@login_required
def reviews(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No user with that username is registered.", category="error")
        return redirect(url_for("views.home"))

    reviews = Review.query.filter_by(creator=user.id).all()
    return render_template("reviews.html", user=current_user, reviews=reviews, username=username)


@views.route("/create_comment/<review_id>", methods=["POST"])
@login_required
def create_comment(review_id):
    content = request.form.get("content")
    if not content:
        flash("The content of a comment cannot be empty.", category="error")
    else:
        review = Review.query.filter_by(id=review_id)
        if review:
            comment = Comment(content=content, creator=current_user.id, review_id=review_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash("The review you are trying to comment on does not exist.", category="error")

    return redirect(url_for("views.home"))


@views.route("/delete_comment/<comment_id>", methods=["GET"])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash("The comment you are trying to delete does not exist.", category="error")
    elif current_user.id != comment.creator and current_user.id != comment.review.creator:
        flash("You do not have permission to delete this comment.", category="error")
    else:
        db.session.delete(comment)
        db.session.commit()
        
    return redirect(url_for("views.home"))
        

    return redirect(url_for("views.home"))


@views.route("/like_review/<review_id>", methods=["GET"])
@login_required
def heart(review_id):
    review = Review.query.filter_by(id=review_id)
    heart = Heart.query.filter_by(creator=current_user.id, review_id=review_id).first()

    if not review:
        flash("The review you are trying to heart does not exist.", category="error")
    elif heart:
        db.session.delete(heart)
        db.session.commit()
    else:
        heart = Heart(creator=current_user.id, review_id=review_id)
        db.session.add(heart)
        db.session.commit() 

    return redirect(url_for("views.home"))