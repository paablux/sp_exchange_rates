import requests
import requests_mock
from extract.request_interface import RequestInterface, BASE_URL
from extract import request_interface
from ratelimit import RateLimitException
import pytest 


request_interface.API_RATE = 1
request_interface.API_CALLS_PER_RATE = 1

def test_request_404(requests_mock):
    requests_mock.get(BASE_URL, status_code=400)
    req = RequestInterface()
    req_result =  req.request_exchange_api()
    with pytest.raises(Exception):
        req.check_response(req_result)

def test_request_429(requests_mock):
    requests_mock.get(BASE_URL, status_code=429)
    req = RequestInterface()
    
    req_result =  req.request_exchange_api()
    with pytest.raises(RateLimitException):
        req.check_response(req_result)

def test_request(requests_mock):
    data = {"rates": {"2020-11-02": {"CAD": 1.5466, "HKD": 9.0327}}}
    requests_mock.get(BASE_URL, json=data)
    req = RequestInterface()
    req.settings = {"api_token": 'aksjhd'}
    assert req.request_exchange_api().json() == data

def test_prepare_request():
    req = RequestInterface()
    req.settings = {"api_token": 'aksjhd'}
    req.prepare_request('EUR')
    assert req.params == {"start_at": "2018-01-01", "end_at": "2021-01-01", "base": "EUR"}
    assert req.headers == {"Authorization": f"Bearer aksjhd"}




