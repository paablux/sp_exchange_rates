from requests import get
from json import dumps

from ratelimit import limits, sleep_and_retry, RateLimitException

from .request_interface import RequestInterface


SYMBOLS = ["USD", "GBP", "EUR"]
RAW_PATH_SAVE = "data/raw"

class Extract():
    def __init__(self):
        # Default interface
        print('starting extractor..')
        self.http_request_interface = RequestInterface
    
    def save_raw_file(self, data, symbol:str): 
        print(f"{RAW_PATH_SAVE}/raw_exchange_{symbol}.json")          
        with open(f"{RAW_PATH_SAVE}/raw_exchange_{symbol}.json", "w+") as f:
            str_data = dumps(data)
            f.write(str_data)
    
    def run(self):
        self.http_request_interface = self.http_request_interface()
        for symbol in SYMBOLS:
            print(f'extracting {symbol}')
            response = self.http_request_interface.run_api_symbol(symbol)
            self.save_raw_file(response, symbol=symbol)
            print(f'saved json raw file for {symbol} exchange rates')
