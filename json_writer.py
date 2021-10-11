import json
from db_helper import read_from_sqlite, write_json_to_sqlite
from file_helper import write_json_to_file
from url_helper import decode_words

def create_json_file():
    measurements = _create_sample_json()
    fileName = 'data\measurements.json'
    write_json_to_file(json.dumps(measurements, indent=4), fileName)
    
def create_json_db_record():
    measurements = _create_sample_json()
    dbName = 'data\measurements.db'
    write_json_to_sqlite(measurements, 'data\measurements.db')
   
def read_db_record():
    dbName = 'data\measurements.db'
    data = read_from_sqlite(dbName)
    print(data)

def create_json_from_url():
    url = 'http://sixty-north.com/c/t.txt'
    url = 'https://gist.githubusercontent.com/corysimmons/8b94c08421dec18bbaa4/raw/9b9814f2efbf09ca11f0588b906ec10f72e67901/the-zen-of-python.txt'
    print('Reading from url: ' + url)
    results = decode_words(url)
    for line in results:
        print(line)

# internal non-public method
def _create_sample_json():
    return [
        {'weight': 392.3, 'color': 'purple', 'temperature': 33.4},
        {'weight': 34.0, 'color': 'green', 'temperature': -3.1}
    ]