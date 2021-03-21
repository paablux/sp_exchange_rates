from csv import reader
from mysql import BaseDB


class Loader():

    def __init__(self):
        self.sql_client = BaseDB

    def load_csv(self):
        csv_data = list()
        headers = list()
        with open('employee_birthday.txt') as csv_file:
            csv_reader = reader(csv_file, delimiter=',')
            for line, row in enumerate(csv_reader):
                if line_count == 0:
                    headers = row
                else:
                    item = {header: item[header] for header in headers}
                    csv_data.append(item)
        return csv_data               
    
    def run():
        data = self.load_csv()
        with self.sql_client() as db:
            db.load(data)
