from flask import Blueprint
from flask import jsonify


api = Blueprint("api", __name__)


@api.route("/api/index/", methods=["GET"])
def index():
    return jsonify({"id": "It Works"})
