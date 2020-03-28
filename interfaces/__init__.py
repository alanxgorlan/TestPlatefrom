from flask import Blueprint
from flask import render_template

interface = Blueprint("interface",
                       __name__,
                       static_folder="static",
                       template_folder="templates",
                       url_prefix="/interface")

@interface.route("/create")
def index():
    return render_template("interface.html")