from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app(*args, **kwargs):
    """
    This function creates the application and is used to run the application.
    """
    # Creating the flask application object.
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

    # Register commands 
    from commands import db_commands
    app.register_blueprint(db_commands)

    # Register routes from application.
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app