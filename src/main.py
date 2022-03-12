from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app(*args, **kwargs):
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)

    from models.models import User

    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    from commands import db_commands
    app.register_blueprint(db_commands)

    # Then we can register our routes!
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app