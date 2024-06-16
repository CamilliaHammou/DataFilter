import csv

def load_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key, value in row.items():
                if value.lower() == 'true':
                    row[key] = True
                elif value.lower() == 'false':
                    row[key] = False
                elif value.isdigit():
                    row[key] = int(value)
                elif value.replace('.', '', 1).isdigit():
                    row[key] = float(value)
                elif value.startswith('[') and value.endswith(']'):
                    row[key] = eval(value)
            data.append(dict(row))
    return data

def save_csv(data, file_path):
    if not data:
        return
    
    fieldnames = data[0].keys()
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        
        for row in data:
            for key, value in row.items():
                if isinstance(value, list):
                    row[key] = str(value)
                elif isinstance(value, bool):
                    row[key] = 'True' if value else 'False'
            writer.writerow(row)