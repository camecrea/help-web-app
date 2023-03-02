from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)


@routes.route("/")
@routes.route("/home")
def home():
    return render_template("home.html")


@routes.route("/login")
def login():
    return render_template("login.html")
