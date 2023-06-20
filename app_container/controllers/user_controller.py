from flask import Flask, Blueprint, request, jsonify
from app_container.models.user import User

user_controller = Blueprint('user', __name__)
user = User()


@user_controller.route('create', methods=['POST'])
def create_user():
    req = request.get_json()
    obj = user.create(req)
    obj['_id'] = str(obj['_id'])
    return jsonify(obj)


@user_controller.route('/get', methods=['GET'])
def get_user():
    params = dict(request.args)
    obj = user.get(params)
    obj['_id'] = str(obj['_id'])
    return jsonify(obj)


@user_controller.route('/fetch', methods=['GET'])
def fetch_users():
    params = dict(request.args)
    obj = user.fetch(params)
    obj = [{**item, "_id": str(item['_id'])} for item in obj]
    return jsonify(obj)
