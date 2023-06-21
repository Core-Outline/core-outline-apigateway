from config.sever_config import servers
from app_container.repositories.request import get, post


class QueryService():
    def __init__(self) -> None:
        pass

    def create_query(self, query):
        return post(
            url=f"{servers[query['type']]}/query/create-query",
            data=query,
            headers={

            },
            params={}
        )

    def get_query_by_id(self, query):
        return get(
            url=f"{servers[query['type']]}'/query/get-query",
            params=query,
            headers={}
        )

    def fetch_query_by_parameter(self, query):
        print(query)
        return get(
            url=f"{servers[query['type']]}/query",
            params=query,
            headers={}
        )
