from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify
from interfaces.services import Services

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
    #对data进行校验,主要校验method和url
    method = data.get('method', None)
    if not method:
        return jsonify({
            "status": 400,
            "message": "invalid parameter 'method'!",
            "data": data
        })
    url = data.get('url', None)
    if not method:
        return jsonify({
            "status": 400,
            "message": "invalid parameter 'url'!",
            "data": data
        })

    service = Services()
    res = service.send_request(data)
    #注意此处jsonify处理的要是python的内置类型，res是自定义的类，所以先把res类型进行变化，由于request返回的是json，所以这里选择直接转换为json
    return jsonify({
        "status" : 200,
        "message" : "ok",
        "data" : res
    })