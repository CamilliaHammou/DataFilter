import csv

def load_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
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
            writer.writerow(row)
