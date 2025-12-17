from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__)


@bp.get("/hello")
def hello():
    name = request.args.get("name", "world")
    return jsonify(message=f"hello {name}")
