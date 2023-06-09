from flask import Flask, Blueprint, request, jsonify
from app.models.user import User

user_controller = Blueprint('user', __name__)
user = User()


@user_controller.route('create', methods=['POST'])
def create_user():
    body = request.get_json()
    return jsonify(user.create(body))


@user_controller.route('/get', methods=['GET'])
def get_user():
    params = dict(request.args)
    return jsonify(user.get(params))


@user_controller.route('/fetch', methods=['GET'])
def fetch_users():
    params = dict(request.args)
    return jsonify(user.fetch(params))
