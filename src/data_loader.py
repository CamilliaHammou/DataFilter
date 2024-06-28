# *********************************************************************************************************** #
#                                                                                                             #
#                                                               :::::::::: ::::::::   :::::::: :::::::::::    #
#    data_loader.py                                            :+:       :+:    :+: :+:    :+:    :+:         #
#                                                             +:+       +:+        +:+           +:+          #
#    By: Camillia <chammou1@myges.fr>                        +#++:++#  +#++:++#++ :#:           +#+           #
#                                                           +#+              +#+ +#+   +#+#    +#+            #
#    Created: 2024/06/25 21:15:45 by Camillia              #+#       #+#    #+# #+#    #+#    #+#             #
#    Updated: 2024/06/25 21:27:22 by Camillia             ########## ########   ######## ###########          #
#                                                                                                             #
# *********************************************************************************************************** #

import csv
import json
from typing import List, Dict, Any
from utils.type_converter import auto_convert
import xml.etree.ElementTree as ET
import yaml

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
        elif file_format == 'xml':
            tree = ET.parse(file_path)
            root = tree.getroot()
            data_filter.data = []
            for student in root.findall('student'):
                student_data = {}
                for elem in student:
                    if elem.tag == 'grades':
                        student_data[elem.tag] = [int(grade.text) for grade in elem.findall('grade')]
                    else:
                        student_data[elem.tag] = auto_convert(elem.text)
                data_filter.data.append(student_data)
        elif file_format == 'yaml':
            with open(file_path, 'r') as yamlfile:
                data_filter.data = yaml.safe_load(yamlfile)
