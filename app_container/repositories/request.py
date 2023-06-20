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

    return response


def post(url, data, params, headers, auth, file):
    response = requests.post(
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

    return response
