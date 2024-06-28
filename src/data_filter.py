# *********************************************************************************************************** #
#                                                                                                             #
#                                                               :::::::::: ::::::::   :::::::: :::::::::::    #
#    data_filter.py                                            :+:       :+:    :+: :+:    :+:    :+:         #
#                                                             +:+       +:+        +:+           +:+          #
#    By: Camillia <chammou1@myges.fr>                        +#++:++#  +#++:++#++ :#:           +#+           #
#                                                           +#+              +#+ +#+   +#+#    +#+            #
#    Created: 2024/06/25 21:15:42 by Camillia              #+#       #+#    #+# #+#    #+#    #+#             #
#    Updated: 2024/06/25 21:15:42 by Camillia             ########## ########   ######## ###########          #
#                                                                                                             #
# *********************************************************************************************************** #

from utils.type_converter import auto_convert
from typing import List, Dict, Any 
from typing import Any, List
import statistics

class DataFilter:
    def __init__(self):
        self.data = []

    def filter_data(self, field: str, operator: str, value: Any = None, field2: str = None):
        if field2:
            self.data = [item for item in self.data if self.compare_fields(item, field, operator, field2)]
        elif operator in ['contains', 'startswith', 'endswith']:
            self.data = [item for item in self.data if self.string_compare(item[field], operator, value)]
        elif operator in ['all', 'any', 'min', 'max', 'avg']:
            self.data = [item for item in self.data if self.list_compare(item[field], operator, value)]
        elif operator in ['above_avg', 'below_avg', 'above_percentile', 'below_percentile']:
            self.data = [item for item in self.data if self.stat_compare(item, field, operator, value)]
        else:
            self.data = [item for item in self.data if self.compare(item[field], operator, auto_convert(value))]

    def compare(self, a: Any, op: str, b: Any) -> bool:
        if isinstance(a, list) and not isinstance(b, list):
            a = len(a)
        if isinstance(b, list) and not isinstance(a, list):
            b = len(b)
        if op == '==': return a == b
        if op == '!=': return a != b
        if op == '<': return a < b
        if op == '<=': return a <= b
        if op == '>': return a > b
        if op == '>=': return a >= b
        return False

    def string_compare(self, a: str, op: str, b: str) -> bool:
        if op == 'contains': return b in a
        if op == 'startswith': return a.startswith(b)
        if op == 'endswith': return a.endswith(b)
        return False

    def list_compare(self, a: List, op: str, b: Any) -> bool:
        b = auto_convert(b)
        if op == 'all': return all(self.compare(x, '>=', b) for x in a)
        if op == 'any': return any(self.compare(x, '>=', b) for x in a)
        if op == 'min': return min(a) == b
        if op == 'max': return max(a) == b
        if op in ['avg']:
            avg = statistics.mean(a)
            if op == 'avg': return abs(avg - float(b)) < 1e-9
        return False

    def compare_fields(self, item: dict, field1: str, op: str, field2: str) -> bool:
        return self.compare(item[field1], op, item[field2])

    def stat_compare(self, item: dict, field: str, op: str, value: float) -> bool:
        all_values = [x[field] for x in self.data if isinstance(x[field], (int, float))]
        if op == 'above_avg':
            return item[field] > statistics.mean(all_values)
        if op == 'below_avg':
            return item[field] < statistics.mean(all_values)
        if op == 'above_percentile':
            return item[field] > statistics.quantiles(all_values, n=100)[int(value)]
        if op == 'below_percentile':
            return item[field] < statistics.quantiles(all_values, n=100)[int(value)]
        return False