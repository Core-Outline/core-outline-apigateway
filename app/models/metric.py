from app.services.metric_service import MetricService


class Metric:
    def __init__(self):
        self.metricService = MetricService()

    def create(self, metric):
        return self.metricService.create_metric(metric)

    def get(self, metric):
        return self.metricService.get_metric(metric)

    def fetch(self, metric):
        return self.metricService.fetch_metric(metric)
