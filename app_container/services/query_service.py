from config.sever_config import servers
from app_container.repositories.request import get, post
from app_container.transformers.mysql import transform_mysql
from app_container.transformers.mongodb import transform_mongodb


class QueryService():
    def __init__(self) -> None:
        pass

    def create_query(self, query):
        print(query)
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
        return get(
            url=f"{servers[query['type']]}/query",
            params=query,
            headers={}
        )

    def execute_query(self, query):
        res = post(
            url=f"{servers[query['type']]}/query/execute",
            data=query,
            params={},
            headers={}
        )
        if query['type'] == 'mysql':
            return transform_mysql(res)
        if query['type'] == 'mongodb':
            return transform_mongodb(res)
