#Run pip install flask-blueprint
from flask import Blueprint
calender_bp = Blueprint('calender',__name__, template_folder = "template")

@calender_bp.route("/")
def home_page():
    return "This is calender home page"
