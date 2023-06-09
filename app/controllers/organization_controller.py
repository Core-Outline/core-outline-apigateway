from flask import Flask, Blueprint, request, jsonify
from app.models.organization import Organization

organization_controller = Blueprint('organization', __name__)
organization = Organization()


@organization_controller.route('create', methods=['POST'])
def create_user():
    body = request.get_json()
    return jsonify(organization.create(body))


@organization_controller.route('/get', methods=['GET'])
def get_user():
    params = dict(request.args)
    return jsonify(organization.get(params))


@organization_controller.route('/fetch', methods=['GET'])
def fetch_users():
    params = dict(request.args)
    return jsonify(organization.fetch(params))
