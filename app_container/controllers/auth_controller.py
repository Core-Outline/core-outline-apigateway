from flask import Blueprint, request, jsonify
from app_container.models.auth import Auth

auth_controller = Blueprint('auth', __name__)
auth = Auth()


@auth_controller.route('/signin', methods=['POST'])
def signin():
    req = request.get_json()
    obj = auth.signin(req)
    return jsonify(obj)


@auth_controller.route('/signup', methods=['POST'])
def signup():
    req = request.get_json()
    obj = auth.signup(req)
    print(obj)
    return jsonify(obj)
