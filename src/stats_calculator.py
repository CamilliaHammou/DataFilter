# *********************************************************************************************************** #
#                                                                                                             #
#                                                               :::::::::: ::::::::   :::::::: :::::::::::    #
#    stats_calculator.py                                       :+:       :+:    :+: :+:    :+:    :+:         #
#                                                             +:+       +:+        +:+           +:+          #
#    By: Camillia <chammou1@myges.fr>                        +#++:++#  +#++:++#++ :#:           +#+           #
#                                                           +#+              +#+ +#+   +#+#    +#+            #
#    Created: 2024/06/25 21:15:52 by Camillia              #+#       #+#    #+# #+#    #+#    #+#             #
#    Updated: 2024/06/25 21:15:52 by Camillia             ########## ########   ######## ###########          #
#                                                                                                             #
# *********************************************************************************************************** #

from typing import Any, List, Dict


class StatsCalculator:
    @staticmethod
    def display_stats(data_filter):
        if not data_filter.data:
            print("Aucune donnée chargée.")
            return

        fields = data_filter.data[0].keys()
        for field in fields:
            values = [item[field] for item in data_filter.data]
            print(f"Champ: {field}")

            if all(isinstance(v, (int, float)) for v in values):
                print(f"  Min: {min(values)}")
                print(f"  Max: {max(values)}")
                print(f"  Moyenne: {sum(values) / len(values):.2f}")
            elif all(isinstance(v, bool) for v in values):
                true_count = sum(values)
                false_count = len(values) - true_count
                print(f"  % Vrai: {true_count / len(values) * 100:.2f}%")
                print(f"  % Faux: {false_count / len(values) * 100:.2f}%")
            elif all(isinstance(v, list) for v in values):
                if all(isinstance(item, (int, float)) for v in values for item in v):
                    flattened = [item for sublist in values for item in sublist]
                    print(f"  Min: {min(flattened)}")
                    print(f"  Max: {max(flattened)}")
                    print(f"  Moyenne globale: {sum(flattened) / len(flattened):.2f}")
                lengths = [len(v) for v in values]
                print(f"  Min longueur: {min(lengths)}")
                print(f"  Max longueur: {max(lengths)}")
                print(f"  Moyenne longueur: {sum(lengths) / len(lengths):.2f}")
            elif all(isinstance(v, str) for v in values):
                print(f"  Nombre de valeurs uniques: {len(set(values))}")
