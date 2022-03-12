from flask import Blueprint, render_template, redirect, url_for, request, flash
from main import db
from models.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Create a blueprint named user which will be used for routes relating to users and authentication.
user = Blueprint("user", __name__)

# Create a route for the login page.
@user.route("/login", methods=["GET", "POST"])
def login():
    """
    This function allows users to both access the login page and creates the necessary functionalities 
    to login into their accounts.

    Parameters:
        GET:/login 
        POST:/login

    Returns:
        It renders the login.html template and redirects users to the homepage if they sign up.
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password is incorrect", category="error")
        else:
            flash("Email is not registered to a user.", category="error")  

    return render_template("login.html", user=current_user)


# Creates a route to access the sign up page and its functionalities.
@user.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    This function allows users to both access the sign up page and creates the necessary functionalities 
    to create a new account.

    Parameters:
        GET:/sign_up 
        POST:/sign_up

    Returns:
        It renders the signup.html template and redirects users to the homepage if they sign up.
    """
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash("Email is already registered to an account.", category="error")
        elif username_exists:
            flash("Username is already registered to an account.", category="error")
        elif password1 != password2:
            flash("The passwords do not match.", category="error")
        elif len(username) < 4:
            flash("Username is too short, usernames need to be 4 characters or greater.", category="error")
        elif len(password1) < 8:
            flash("Password is too short, passwords need to be 8 characters or greater.", category="error")
        elif len(email) < 5:
            flash("Email is invalid.", category="error")
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Successfully created and logged in user.')
            return redirect(url_for("views.home"))

    
    return render_template("signup.html", user=current_user)

# Creates a route to allow users to logout.
@user.route("/log_out", methods=["GET"])
# Users have to be logged in to access this functionality.
@login_required
def log_out():
    """
    This function allows users sign out of their account.

    Parameters:
        GET:/log_out 

    Returns:
        It redirects users to the homepage if they choose to log out.
    """
    logout_user()
    return redirect(url_for("views.home"))