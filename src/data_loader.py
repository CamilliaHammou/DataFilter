import csv
import json
from typing import List, Dict, Any
from utils.type_converter import auto_convert

class DataLoader:
    @staticmethod
    def load_data(data_filter, file_path: str, file_format: str):
        if file_format == 'csv':
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                data_filter.data = [{k: auto_convert(v) for k, v in row.items()} for row in reader]
        elif file_format == 'json':
            with open(file_path, 'r') as jsonfile:
                data_filter.data = json.load(jsonfile)
