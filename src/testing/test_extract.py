from extract.extract import Extract
from extract import extract
import pytest
import os

@pytest.fixture()
def resource():
    print("setup")
    yield "resource"
    print("teardown")
    os.remove('src/testing/fixtures/raw_exchange_FAKE.json')

def test_save_raw_file(resource):
    RAW_PATH_SAVE = 'src/testing/fixtures'
    extract.RAW_PATH_SAVE = RAW_PATH_SAVE
    input_data = {"data": ["item", "item_2"]}
    expected_file_data = '{"data": ["item", "item_2"]}'
    extractor = Extract()
    extractor.save_raw_file(input_data, 'FAKE')
    with open('src/testing/fixtures/raw_exchange_FAKE.json') as f:
        assert f.read() == expected_file_data

