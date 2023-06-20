from config.sever_config import servers
from app_container.repositories.request import get, post


class DataSourceService():
    def __init__(self) -> None:
        pass

    def create_data_source(self, data_source):
        return post(
            url=f"{servers[data_source.type]}/data-source/create-data-source",
            data=data_source,
        )

    def get_data_source_by_id(self, data_source):
        return get(
            url=f"{servers[data_source.type]}'data-source/get-data-source",
            params=data_source
        )

    def fetch_data_sources_by_parameter(self, data_source):
        return get(
            url=f"{servers[data_source.type]}/data-source/data-source",
            params=data_source
        )
