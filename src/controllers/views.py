from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models.models import Review, User, Comment, Heart
from main import db

# Create a blueprint named views which will be used for routes relating to the reviews.
views = Blueprint("views", __name__)

# Creates two routes via which the user can access the homepage.
@views.route("/home", methods=["GET"])
@views.route("/", methods=["GET"])
@login_required
# Users have to be logged in to access this functionality.
def home():
    """
    This function allows users to access the homepage which contains all previous reviews created
    on the site.

    Parameters:
        GET:/home

    Returns:
        It renders the home.html template.
    """
    reviews = Review.query.all()
    return render_template("home.html", name=current_user.username, user=current_user, reviews=reviews)


# Create a route for users to create their own reviews on the site.
@views.route("/create_review", methods=["GET", "POST"])
@login_required
# Users have to be logged in to access this functionality.
def create_review():
    """
    This function allows users to access the page which lets them create their own and submit them to the site.

    Parameters:
        GET:/create_review
        POST:/create_review

    Returns:
        It renders the create_review.html template and redirects users to the homepage if they choose to create
        a review.
    """
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


# Create a route for users to delete reviews.
@views.route("/delete_review/<id>", methods=["GET"])
@login_required
# Users have to be logged in to access this functionality.
def delete_review(id):
    """
    This function allows users to delete a review which they have created.
    
    Parameters:
        GET:/delete_review

    Returns:
        It renders the home.html template.
    """
    review = Review.query.filter_by(id=id).first()

    if not review:
        flash("The review you are trying to delete does not exist.", category="error")
    else:
        db.session.delete(review)
        db.session.commit()
        flash("The review has been successfully deleted.", category="success")

    return redirect(url_for("views.home"))


# Create a route which displays all reviews created by a single user.
@views.route("/reviews/<username>", methods=["GET"])
@login_required
# Users have to be logged in to access this functionality.
def reviews(username):
    """
    This function allows users to access any users' individual page which contains all the reviews
    that user has created on the site.

    Parameters:
        GET:/reviews/<username>

    Returns:
        It renders the reviews.html template.
    """
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No user with that username is registered.", category="error")
        return redirect(url_for("views.home"))

    reviews = Review.query.filter_by(creator=user.id).all()
    return render_template("reviews.html", user=current_user, reviews=reviews, username=username)


# Create a route for users to comment on a review.
@views.route("/create_comment/<review_id>", methods=["POST"])
@login_required
# Users have to be logged in to access this functionality.
def create_comment(review_id):
    """
    This function allows users to create comments on reviews.

    Parameters:
        GET:/create_comment/<review_id>

    Returns:
        It renders the home.html template.
    """
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


# Create a route for users to delete existing comments.
@views.route("/delete_comment/<comment_id>", methods=["GET"])
@login_required
# Users have to be logged in to access this functionality.
def delete_comment(comment_id):
    """
    This function allows users to delete comments on reviews, users only have access to this
    feature if they are the original poster of the comment.

    Parameters:
        GET:/delete_comment/<comment_id>

    Returns:
        It renders the home.html template.
    """
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash("The comment you are trying to delete does not exist.", category="error")
    elif current_user.id != comment.creator and current_user.id != comment.review.creator:
        flash("You do not have permission to delete this comment.", category="error")
    else:
        db.session.delete(comment)
        db.session.commit()
        
    return redirect(url_for("views.home"))


# Create a route for users to heart a review.
@views.route("/heart_review/<review_id>", methods=["GET"])
@login_required
# Users have to be logged in to access this functionality.
def heart(review_id):
    """
    This function allows users to heart and unheart reviews.
    
    Parameters:
        GET:/heart_review/<review_id>

    Returns:
        It renders the home.html template.
    """
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