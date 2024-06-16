from utils import csv_handler

file_path = 'data/data.csv'
data_loaded = csv_handler.load_csv(file_path)
print("Données chargées depuis le fichier CSV :")
print(data_loaded)


data_modified = data_loaded

new_file_path = 'data/data_modified.csv'
csv_handler.save_csv(data_modified, new_file_path)
print(f"Données sauvegardées dans le fichier CSV : {new_file_path}")
