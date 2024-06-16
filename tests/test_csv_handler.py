import unittest
import os
import sys
import csv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import csv_handler

class TestCSVHandler(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'tests/test_data.csv'
        self.create_csv_file()

    def tearDown(self):
        self.delete_csv_file()

    def create_csv_file(self):
        with open(self.test_file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'age'])
            writer.writeheader()
            writer.writerow({'id': '1', 'name': 'Cams', 'age': '20'})
            writer.writerow({'id': '2', 'name': 'Sog', 'age': '25'})

    def delete_csv_file(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_load_csv(self):
        data = csv_handler.load_csv(self.test_file_path)
        expected_data = [
            {'id': '1', 'name': 'Cams', 'age': '20'},
            {'id': '2', 'name': 'Sog', 'age': '25'}
        ]

        for row in expected_data:
            row['id'] = int(row['id'])
            row['age'] = int(row['age'])

        self.assertEqual(data, expected_data)


    def test_save_csv(self):
        data_to_save = [
            {'id': '3', 'name': 'Charlie', 'age': '35'},
            {'id': '4', 'name': 'Diana', 'age': '28'}
        ]

        test_save_path = 'tests/test_save_data.csv'
        csv_handler.save_csv(data_to_save, test_save_path)

        saved_data = csv_handler.load_csv(test_save_path)
        expected_saved_data = [
            {'id': str(row['id']), 'name': str(row['name']), 'age': str(row['age'])}
            for row in data_to_save
        ]

        converted_saved_data = [
            {'id': str(row['id']), 'name': str(row['name']), 'age': str(row['age'])}
            for row in saved_data
        ]

        self.assertEqual(converted_saved_data, expected_saved_data)

        if os.path.exists(test_save_path):
            os.remove(test_save_path)




if __name__ == '__main__':
    unittest.main()
