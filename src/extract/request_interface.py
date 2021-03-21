from requests import get

from ratelimit import limits, sleep_and_retry, RateLimitException

from src.utils.settings import read_settings

BASE_URL = "https://api.exchangeratesapi.io/history"
BASE_PARAMS = {"start_at": "2018-01-01", "end_at": "2021-01-01"}
API_RATE = 60
API_CALLS_PER_RATE = 1

class RequestInterface():
    def __init__(self):
        self.get = get
        self.settings = read_settings()
        self.params = dict()
        self.headers = dict()
    
    def prepare_request(self)
        self.params = {**BASE_PARAMS, **{"base": symbol}}
        # In case we needed a api token (this is not used)
        self.headers = {"Authorization": f"Bearer {self.settings['api_token']}"}
    
    @sleep_and_retry
    @limits(calls=API_CALLS_PER_RATE, period=API_RATE)
    def request_exchange_api(self):
        res = get(BASE_URL, params=self.params)
        return res
    
    def check_response(self, res):
        if res.status_code !=  200:
            if res.status_code == 429:
                # This exception will make the process sleep for 1 second 
                raise RateLimitException('Excessive query behavior detected', 1)
            else:
                raise Exception(f'ERROR in api call status_code: {res.status_code}, {res.text}')
        else:
            if not sinstance(res.json(), dict):
                raise Exception('ERROR in api response: not a json')

    def run_api_symbol(self, symbol):
        # main function that queries api
        self.prepare_request()
        api_response = self.request_exchange_api(symbol)
        self.check_response(res)
        return response
        