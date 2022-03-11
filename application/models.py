from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    """
    A class for the User model used in the program.

    Attributes:
        id (integer): The id that the user will be assigned.
        email (string): The email registered to the user.
        username (string): The username registered to the user.
        password (string): The password registered to the user's account.
        reviews (related to Review model): A one to many relationship which dictates which reviews
        the user has written.
        comments (related to Comment model): A one to many relationship which dictates which comments
        the user has written.
        hearts (related to Heart model): A one to many relationship which dictates which reviews
        the user has hearted.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    reviews = db.relationship("Review", backref="user", passive_deletes=True)
    comments = db.relationship("Comment", backref="user", passive_deletes=True)
    hearts = db.relationship("Heart", backref="user", passive_deletes=True)


class Review(db.Model):
    """
    A class for the Review model used in the program.

    Attributes:
        id (integer): The id that the review will be assigned.
        title (text): The title of the review.
        content (text): The content of the review.
        destination (text): The destination of the review.
        category (text): The category of the review.
        price (string): The price of the review.
        creation_date (datetime): The date at which the review was created.
        creator (related to User model): A many to one relationship which dictates which user wrote
        which reviews.
        comments (related to Comment model): A one to many relationship which dictates which comments
        are related to the review.
        hearts (related to Heart model): A one to many relationship which dictates which hearts
        are related to the review.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    destination = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    price = db.Column(db.String(10), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    creator = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    comments = db.relationship("Comment", backref="review", passive_deletes=True)
    hearts = db.relationship("Heart", backref="review", passive_deletes=True)


class Comment(db.Model):
    """
    A class for the Comment model used in the program.

    Attributes:
        id (integer): The id that the comment will be assigned.
        content (text): The content of the comment.
        creation_date (datetime): The date at which the comment was created.
        creator (related to User model): A one to many relationship which dictates which user wrote
        which reviews.
        creator (related to Comment model): A many to one relationship which dictates which user
        created which comments.
        review_id (related to Review model): A one to many relationship which dictates which comments
        relate to which review.
    """
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    creator = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey("review.id", ondelete="CASCADE"), nullable=False)


class Heart(db.Model):
    """
    A class for the Heart model used in the program.

    Attributes:
        id (integer): The id that the heart will be assigned.
        creator (related to Comment model): A many to one relationship which dictates which user
        hearted which reviews.
        review_id (related to Review model): A one to many relationship which dictates which hearts
        relate to which review.
    """
    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey("review.id", ondelete="CASCADE"), nullable=False)
