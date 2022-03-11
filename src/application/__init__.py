from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """
    This function creates the application and is used when running the app.
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "some secret string"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    # Import both the controllers for views and user
    from .views import views
    from .user import user

    # Registers the two blueprints for the site
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(user, url_prefix="/")

    # Imports models used in the application
    from .models import User, Review, Comment, Heart

    # Creates the databse
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    """
    This function creates the database used in the application.

    Returns:
        It creates the database.
    """
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")