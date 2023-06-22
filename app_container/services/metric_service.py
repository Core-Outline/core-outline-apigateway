from app_container.repositories.database import createClient, create, get, fetch
from app_container.repositories.request import post

from config.metric_config import metric_table, metrics
from config.sever_config import servers


class MetricService:
    def __init__(self):
        self.db = createClient()

    def create_metric(self, metric):
        return create(self.db, metric_table, metric)

    def get_metric(self, metric):
        return get(self.db, metric_table, metric)

    def fetch_metric_by_parameter(self, metric):
        return fetch(self.db, metric_table, metric)

    def execute_metric(self, metric):
        return post(
            url=f"{servers['ml']}/{metrics[metric['metric_type']]}",
            data=metric,
            headers={

            },
            params={}
        )
