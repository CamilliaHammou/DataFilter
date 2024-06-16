import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    for item in data:
        for key, value in item.items():
            if isinstance(value, str) and value.lower() == 'true':
                item[key] = True
            elif isinstance(value, str) and value.lower() == 'false':
                item[key] = False
            elif isinstance(value, str) and value.isdigit():
                item[key] = int(value)
            elif isinstance(value, str) and value.replace('.', '', 1).isdigit():
                item[key] = float(value)
            elif isinstance(value, str) and value.startswith('[') and value.endswith(']'):
                item[key] = eval(value)
    
    return data


def save_json(data, file_path):
    for item in data:
        for key, value in item.items():
            if isinstance(value, list):
                item[key] = str(value)
            elif isinstance(value, bool):
                item[key] = str(value)
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
