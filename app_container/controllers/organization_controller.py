from flask import Flask, Blueprint, request, jsonify
from app_container.models.organization import Organization

organization_controller = Blueprint('organization', __name__)
organization = Organization()


@organization_controller.route('create', methods=['POST'])
def create_user():
    req = request.get_json()
    obj = organization.create(req)
    obj['_id'] = str(obj['_id'])
    return jsonify(obj)


@organization_controller.route('/get', methods=['GET'])
def get_user():
    params = dict(request.args)
    obj = organization.get(params)
    obj['_id'] = str(obj['_id'])
    return jsonify(obj)


@organization_controller.route('/fetch', methods=['GET'])
def fetch_users():
    params = dict(request.args)
    obj = organization.fetch(params)
    obj = [{**item, "_id": str(item['_id'])} for item in obj]
    return jsonify(obj)
