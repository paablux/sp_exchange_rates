from os import listdir
from os.path import isfile, join
from datetime import datetime
from csv import writer
from json import loads

RAW_DATA_PATH = "data/raw/"

def get_api_raw_file_names():
    files = list()
    for item in listdir(RAW_DATA_PATH):
        file_name = join(RAW_DATA_PATH, item)
        files.append(file_name)
    return files

def read_extracted_files(files):
    content = list()
    for file_name in files:
        with open(file_name, 'r') as f:
            item_dict = loads(f.read())
            content.append(item_dict)
    return content


def parse_file(data:dict):
    symbol = data['base']
    parsed_data = list()
    for date_str, values in data["rates"].items():
        item_parsed = dict()
        item_parsed['date'] = datetime.strptime(date_str, "%Y-%m-%d")
        item_parsed['base_currency'] = symbol
        item_parsed = {**item_parsed, **values}
        parsed_data.append(item_parsed)
    return parsed_data


def order_items_by_date(data:list, is_desc:bool):
    return sorted(data, key=lambda k: k['date'], reverse=is_desc)

def prepare_data_csv(data):
    # create a list of lists from the list of dictionaries in the parsed data
    if not data:
        raise Exception('Empty data')
    csv_data = list()
    for currency_item in data:
        csv_columns = list(currency_item[0].keys())
        rows = list()
        for item in currency_item:
            row = list()
            for column in csv_columns:
                if column != 'date':
                    row += (item.get(column, None),)
                else:
                    row += (item[column].strftime('%d/%m/%Y'),)
            rows.append(row)
        csv_data.append([csv_columns, rows, ])
    return csv_data
    
def find_base_currency(columns, rows):
    sample = {key: value for key, value in zip(columns, rows[0])}
    return sample['base_currency']

def convert_to_csv(columns, rows):
    currency = find_base_currency(columns, rows)
    epoch_time = int(datetime.now().timestamp())
    with open(f'data/extracted/extracted_exchanges_{currency}.csv', 'w') as f: 
        write = writer(f)
        write.writerow(columns)
        write.writerows(rows)

def run():
    print("CSV transform started")
    file_names = get_api_raw_file_names()
    raw_content = read_extracted_files(file_names)
    parsed_data = [parse_file(item) for item in raw_content]
    csv_ready_data = prepare_data_csv(parsed_data)
    for data in csv_ready_data:
        convert_to_csv(*data)
    print('Parsed & csv saved')

    

