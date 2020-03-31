from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify

interface = Blueprint("interface",
                       __name__,
                       static_folder="static",
                       template_folder="templates",
                       url_prefix="/interface")

@interface.route("/create")
def index():
    return render_template("interface.html")

@interface.route("/api/debug", methods=['POST'])
def debug():
    data = request.get_json()

    return jsonify({
        "status" : 200,
        "message" : "ok",
        "data" : data
    })