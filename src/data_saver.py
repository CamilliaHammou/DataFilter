import csv
import json

class DataSaver:
    @staticmethod
    def save_data(data_filter, file_path: str, file_format: str):
        if file_format == 'csv':
            with open(file_path, 'w', newline='') as csvfile:
                if data_filter.data:
                    writer = csv.DictWriter(csvfile, fieldnames=data_filter.data[0].keys())
                    writer.writeheader()
                    writer.writerows(data_filter.data)
        elif file_format == 'json':
            with open(file_path, 'w') as jsonfile:
                json.dump(data_filter.data, jsonfile, indent=2)
