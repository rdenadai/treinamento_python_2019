from flask import Blueprint
from flask import jsonify


api = Blueprint("api", __name__)


@api.route("/index/", methods=["POST"])
def call_record(data):
    return jsonify({"id": "It Works"})
