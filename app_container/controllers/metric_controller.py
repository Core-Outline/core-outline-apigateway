from flask import Blueprint, request, jsonify
from app_container.models.metric import Metric

metric_controller = Blueprint('metric', __name__)
metric = Metric()


@metric_controller.route('/', methods=['GET'])
def fetch_metrics():
    params = dict(request.args)
    return jsonify(metric.fetch(params))


@metric_controller.route('/create-metric', methods=['POST'])
def create_metric():
    body = request.get_json()
    return jsonify(metric.create(body))


@metric_controller.route('/get-metric', methods=['GET'])
def get_metric():
    params = dict(request.args)
    return jsonify(metric.get(params))
