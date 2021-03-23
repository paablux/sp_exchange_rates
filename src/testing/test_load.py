from load.load import Loader
from load import load
from datetime import datetime
def test_prepare_db():
    fake_loader = Loader()
    input_data = [{'base_currency': 'USD', "USD": 1, "EUR": 0.82, "GBP": 0.75, 'date': '12/02/2021'}, {'base_currency': 'USD', "USD": 1, "EUR": 0.89, "GBP": 0.72, 'date': '12/03/2021'}]
    expected = [
        {"to_exchange_currency": "EUR",
         "exchange_rate": 0.82,
         "date": datetime(2021,2,12),
         "base_currency": "USD"},
        {"to_exchange_currency": "GBP",
         "exchange_rate": 0.75,
         "date": datetime(2021,2,12),
         "base_currency": "USD"},
        {"to_exchange_currency": "EUR",
         "exchange_rate": 0.89,
         "date": datetime(2021,3,12),
         "base_currency": "USD"},
        {"to_exchange_currency": "GBP",
         "exchange_rate": 0.72,
         "date": datetime(2021,3,12),
         "base_currency": "USD"},
    ]
    result = fake_loader.prepare_db(input_data)
    assert expected == result

def test_get_transformed_file_names():
    TRANSFORMED_DATA_PATH = "src/testing/fixtures/"
    load.TRANSFORMED_DATA_PATH = TRANSFORMED_DATA_PATH
    fake_loader = Loader()
    expected = ["src/testing/fixtures/fake_csv.csv"]
    result = fake_loader.get_transformed_file_names()
    assert result == expected