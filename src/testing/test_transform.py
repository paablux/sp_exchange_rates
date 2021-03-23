
from transform.transform import find_base_currency, prepare_data_csv, order_items_by_date
from datetime import datetime


def test_find_base_currency():
    input_data = (['date','base_currency','CAD','HKD','ISK','PHP'], [['2020/02/02', 'EUR', 3.12, 22.2, 0.32, 5.5],])
    expected = 'EUR'
    result = find_base_currency(*input_data)
    assert expected == result

def test_order_items_by_date():
    input_data = [{'date':datetime(2021,2,2), 'currency':'GBP'},{'date':datetime(2021,2,12), 'currency':'GBP'},{'date':datetime(2021,6,2), 'currency':'GBP'}]
    expected = [{'date':datetime(2021,2,2), 'currency':'GBP'},{'date':datetime(2021,2,12), 'currency':'GBP'}, {'date':datetime(2021,6, 2), 'currency':'GBP'}]
    result = order_items_by_date(input_data, False)
    assert expected == result
    input_data = [{'date':datetime(2021,12,2), 'currency':'GBP'},{'date':datetime(2021,12,12), 'currency':'GBP'},{'date':datetime(2021,6,2), 'currency':'GBP'}]
    expected = [{'date':datetime(2021,6,2), 'currency':'GBP'}, {'date':datetime(2021,12,2), 'currency':'GBP'}, {'date':datetime(2021,12,12), 'currency':'GBP'}]
    result = order_items_by_date(input_data, False)
    assert expected == result

def test_prepare_data_csv():
    pass