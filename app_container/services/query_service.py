from config.sever_config import servers
from app_container.repositories.request import get, post


class QueryService():
    def __init__(self) -> None:
        pass

    def create_query(self, query):
        return post(
            url=f"{servers[query.type]}/query/create-query",
            data=query,
        )

    def get_query_by_id(self, data_source):
        return get(
            url=f"{servers[data_source.type]}'/query/get-query",
            params=data_source
        )

    def fetch_data_sources_by_parameter(self, data_source):
        return get(
            url=f"{servers[data_source.type]}/query/query",
            params=data_source
        )
