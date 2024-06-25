from utils.type_converter import auto_convert
from typing import List, Dict, Any 

class DataFilter:
    def __init__(self):
        self.data = []

    def filter_data(self, field: str, operator: str, value: Any):
        value = auto_convert(value)
        
        def compare(a, b, op):
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

        self.data = [item for item in self.data if compare(item[field], value, operator)]
