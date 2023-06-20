from app_container.repositories.database import createClient, create, get, fetch

from config.metric_config import metric_table


class MetricService:
    def __init__(self):
        self.db = createClient()

    def create_data_source(self, metric):
        return create(self.db, metric_table, metric)

    def get_data_source(self, metric):
        return get(self.db, metric_table, metric)

    def fetch_metric_by_parameter(self, metric):
        return get(self.db, metric_table, metric)
