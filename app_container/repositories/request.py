import requests
from config.app_configs import auth_token


def get(url, data, params, headers, auth):
    response = requests.get(
        url,
        data,
        params,
        auth,
        headers={
            **{
                'Authorization': f'Bearer {auth_token}'
            },
            **headers
        },
    )

    return response.json()


def post(url, data, params, headers):
    response = requests.post(
        url=url,
        data=data,
        params=params,
        headers={
            **{
                'Authorization': f'Bearer {auth_token}'
            },
            **headers
        },
    )
    print(response)

    return response.json()
