import unittest
import os
import sys
import csv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import csv_handler

class TestCSVHandler(unittest.TestCase):

    def setUp(self):  # This method is called before each test
        self.test_file_path = 'tests/test_data.csv'
        self.create_csv_file()

    def tearDown(self):  # This method is called after each test, FAIL OR PASS 
        self.delete_csv_file()

    def create_csv_file(self):  # Create a fictive csv file
        with open(self.test_file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'age'])
            writer.writeheader()
            writer.writerow({'id': '1', 'name': 'Cams', 'age': '20'})
            writer.writerow({'id': '2', 'name': 'Sog', 'age': '25'})

    def delete_csv_file(self):  # Delete the fictive file after testing
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_load_csv(self):  # Test to see if load function works
        data = csv_handler.load_csv(self.test_file_path)
        expected_data = [
            {'id': '1', 'name': 'Cams', 'age': '20'},
            {'id': '2', 'name': 'Sog', 'age': '25'}
        ]
        self.assertEqual(data, expected_data)

    def test_save_csv(self):  # Test to see if it saves well
        data_to_save = [
            {'id': '3', 'name': 'Charlie', 'age': '35'},
            {'id': '4', 'name': 'Diana', 'age': '28'}
        ]
        test_save_path = 'tests/test_save_data.csv'
        csv_handler.save_csv(data_to_save, test_save_path)

        # Verify if the file was saved correctly
        saved_data = csv_handler.load_csv(test_save_path)
        self.assertEqual(saved_data, data_to_save)

        # Clean the test by deleting the saved file
        if os.path.exists(test_save_path):
            os.remove(test_save_path)

if __name__ == '__main__':
    unittest.main()