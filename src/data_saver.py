# *********************************************************************************************************** #
#                                                                                                             #
#                                                               :::::::::: ::::::::   :::::::: :::::::::::    #
#    data_saver.py                                             :+:       :+:    :+: :+:    :+:    :+:         #
#                                                             +:+       +:+        +:+           +:+          #
#    By: Camillia <chammou1@myges.fr>                        +#++:++#  +#++:++#++ :#:           +#+           #
#                                                           +#+              +#+ +#+   +#+#    +#+            #
#    Created: 2024/06/25 21:15:47 by Camillia              #+#       #+#    #+# #+#    #+#    #+#             #
#    Updated: 2024/06/25 21:15:47 by Camillia             ########## ########   ######## ###########          #
#                                                                                                             #
# *********************************************************************************************************** #

import csv
import json
import xml.etree.ElementTree as ET

class DataSaver:
    @staticmethod
    def save_data(data_filter, file_path: str, file_format: str):
        if file_format == 'csv':
            with open(file_path, 'w', newline='') as csvfile:
                if data_filter.data:
                    fieldnames = data_filter.data[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in data_filter.data:
                        writer.writerow(row)
        elif file_format == 'json':
            with open(file_path, 'w') as jsonfile:
                json.dump(data_filter.data, jsonfile, indent=2)
        elif file_format == 'xml':
            root = ET.Element("data")
            for student in data_filter.data:
                student_elem = ET.SubElement(root, "student")
                for key, value in student.items():
                    if key == 'grades':
                        grades_elem = ET.SubElement(student_elem, "grades")
                        for grade in value:
                            grade_elem = ET.SubElement(grades_elem, "grade")
                            grade_elem.text = str(grade)
                    else:
                        elem = ET.SubElement(student_elem, key)
                        elem.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(file_path, encoding="utf-8", xml_declaration=True)
