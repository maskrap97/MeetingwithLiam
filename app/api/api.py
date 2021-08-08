from flask import Blueprint, json, jsonify, request
from ..model import model
api = Blueprint('admin', __name__, url_prefix='/admin')

@api.route('/', methods=["POST", "GET"])
def api_main():
    print(request.data)
    return jsonify(model(request.data))