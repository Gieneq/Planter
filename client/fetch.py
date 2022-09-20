import requests
from requests.auth import HTTPBasicAuth

ENDPOINT_PATH = 'http://0.0.0.0:5000/' # todo zapisz do .env i zrob konende

# todo zrob dekorator albo cos do rejestrowania
# todo albo sptawdzania czy jest zalgowoany
# f3624a3ad006cc56262f793ca099170013e749fe # token dla pyrograf

def fetch_api_key(username, password):
    endpoint = ENDPOINT_PATH + 'info/api_token/'

    authentication = HTTPBasicAuth(username, password)
    # # POST method - can generate new API key if user already don't have
    # response = requests.post(endpoint, auth=authentication)

    authentication = {
        'username': username,
        'password': password,
    }
    response = requests.post(endpoint, json=authentication)
    # POST method - can generate new API key if user already don't have
    # response = requests.post(endpoint,verify=False, auth=authentication)
    if response.status_code == 200 and hasattr(response, 'json'):
        return response.json().get('token')
    return None

def fetch_register(username, password, email):
    endpoint = ENDPOINT_PATH + 'api/users/create/'
    headers = {
        'username': username,
        'password': password,
        'email': email,
    }
    response = requests.post(endpoint, json=headers)


def fetch_status(verbose=False):
    endpoint = ENDPOINT_PATH + 'info/status/'
    response = requests.get(endpoint)
    if verbose:
        return f"{'Server is OK' if response.status_code == 200 else 'Server encountered problem'} with status code: {response.status_code}."
    return response.status_code

def check_user_apikey(username, api_key):
    endpoint = ENDPOINT_PATH + 'info/api_check/'
    authentication = {"Authorization": f"Token {api_key}"}
    # print(authentication)
    response = requests.get(endpoint, headers=authentication)
    # print(response.status_code, response.headers)
    return response.status_code == 200

# def fetch_date_time(timezone='UTC'):
#     endpoint = ENDPOINT_PATH + 'info/time/'
#     params = {'timezone': timezone}
#     data = requests.get(endpoint, params=params)
#     if data.status_code == 200:
#         return data.json()
#     return None


# def fetch_timezones_list():
#     endpoint = ENDPOINT_PATH + 'info/timezones/'
#     data = requests.get(endpoint)
#     if data.status_code == 200:
#         return data.json()
#     return None
