from os import listdir
from os.path import isfile, join
from csv import reader
from .mysql import BaseDB
from datetime import datetime


TRANSFORMED_DATA_PATH = "data/extracted/"
class Loader():

    def __init__(self):
        self.sql_client = BaseDB

    def load_csv(self, name):
        csv_data = list()
        headers = list()
        with open(name, 'r') as csv_file:
            csv_reader = reader(csv_file, delimiter=',')
            for line, row in enumerate(csv_reader):
                if line == 0:
                    headers = row
                else:
                    item = {header: value for header, value in zip(headers, row)}
                    csv_data.append(item)
        return csv_data

    def get_transformed_file_names(self):
        files = list()
        for item in listdir(TRANSFORMED_DATA_PATH):
            file_name = join(TRANSFORMED_DATA_PATH, item)
            print(file_name[0:-1:3])
            if file_name[::-1][3::-1] == '.csv':
                files.append(file_name)
        return files   

    def prepare_db(self, data):
        key_values = ['base_currency', 'date']
        dataset = list()
        for item in data:
            exchanges_items = list()
            for key, value in item.items():
                if key in key_values:
                    continue
                if key == item["base_currency"]:
                    continue
                exchanges_items.append({
                    "to_exchange_currency": key, "exchange_rate": value,
                     "date": datetime.strptime(item["date"], '%d/%m/%Y'), "base_currency": item["base_currency"] })
            dataset += exchanges_items
        return dataset

    def run(self):
        file_names = self.get_transformed_file_names()
        for file_name in file_names:
            data = self.load_csv(file_name)
            to_db = self.prepare_db(data)
            with self.sql_client() as db:
                db.load(to_db)
