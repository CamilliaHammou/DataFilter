import unittest
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import json_handler

class TestJSONHandler(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'tests/test_data.json'
        self.create_json_file()

    def tearDown(self):
        self.delete_json_file()

    def create_json_file(self):
        data = [
            {'id': '1', 'name': 'Cams', 'age': 20},
            {'id': '2', 'name': 'Sog', 'age': 25}
        ]
        with open(self.test_file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def delete_json_file(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_load_json(self):
        data = json_handler.load_json(self.test_file_path)
        expected_data = [
            {'id': 1, 'name': 'Cams', 'age': 20},
            {'id': 2, 'name': 'Sog', 'age': 25}
        ]
        self.assertEqual(data, expected_data)

    def test_save_json(self):
        data_to_save = [
            {'id': 3, 'name': 'Charlie', 'age': 35},
            {'id': 4, 'name': 'Diana', 'age': 28}
        ]
        test_save_path = 'tests/test_save_data.json'
        json_handler.save_json(data_to_save, test_save_path)

        with open(test_save_path, 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, data_to_save)

        if os.path.exists(test_save_path):
            os.remove(test_save_path)

if __name__ == '__main__':
    unittest.main()
