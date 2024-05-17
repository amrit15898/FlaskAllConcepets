
from flask import Blueprint, render_template, redirect
helloworld_bp = Blueprint('helloword',__name__, template_folder = "templates")


@helloworld_bp.route("/")
def home_page():
    return "This is home page"


@helloworld_bp.route("/about")
def about_page():
    return "about page"

@helloworld_bp.route("/contact_us")
def contact_page():
    return render_template("contact.html")

        


