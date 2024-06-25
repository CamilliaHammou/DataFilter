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
