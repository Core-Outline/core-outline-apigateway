from flask import Blueprint, request, jsonify
from app_container.models.auth import Auth

auth_controller = Blueprint('auth', __name__)
auth = Auth()


@auth_controller.route('/signin', methods=['POST'])
def signin():
    body = request.get_json()
    return jsonify(auth.signin(body))


@auth_controller.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    return jsonify(auth.signup(body))
