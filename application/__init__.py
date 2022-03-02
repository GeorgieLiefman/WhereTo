from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "some secret string"

    from .views import views

    app.register_blueprint(views, url_prefix="/")
    auth.register_blueprint(views, url_prefix="/")

    return app