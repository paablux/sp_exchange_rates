from requests import get
from json import dumps

from ratelimit import limits, sleep_and_retry, RateLimitException

from request_interface import RequestInterface


SYMBOLS = ["USD", "GBP", "EUR"]

class Extract():
    def __init__(self):
        # Default interface
        self.http_request_interface = RequestInterface
    
    def save_raw_file(self, data, symbol:str):            
        with open(f"data/raw_exchange_{symbol}.json", "w+") as f:
            str_data = dumps(data)
            f.write(str_data)
    
    def run(self):
        self.http_request_interface = self.http_request_interface()
        for symbol in SYMBOLS:
            response = self.http_request_interface.run_api_symbol(symbol)
            self.save_raw_file(response.json(), symbol=symbol)
