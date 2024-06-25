# *********************************************************************************************************** #
#                                                                                                             #
#                                                               :::::::::: ::::::::   :::::::: :::::::::::    #
#    main.py                                                   :+:       :+:    :+: :+:    :+:    :+:         #
#                                                             +:+       +:+        +:+           +:+          #
#    By: Camillia <chammou1@myges.fr>                        +#++:++#  +#++:++#++ :#:           +#+           #
#                                                           +#+              +#+ +#+   +#+#    +#+            #
#    Created: 2024/06/25 21:16:01 by Camillia              #+#       #+#    #+# #+#    #+#    #+#             #
#    Updated: 2024/06/25 21:27:27 by Camillia             ########## ########   ######## ###########          #
#                                                                                                             #
# *********************************************************************************************************** #

from src.data_loader import DataLoader
from src.data_saver import DataSaver
from src.stats_calculator import StatsCalculator
from src.data_filter import DataFilter
from src.data_sorter import DataSorter
from src.data_displayer import DataDisplayer

def main():
    data_filter = DataFilter()
    
    while True:
        print("\nOptions:")
        print("1. Charger des données")
        print("2. Sauvegarder les données")
        print("3. Afficher les statistiques")
        print("4. Filtrer les données")
        print("5. Trier les données")
        print("6. Afficher les données")
        print("7. Quitter")
        
        choice = input("Choisissez une option: ")
        
        if choice == '1':
            file_path = input("Entrez le chemin du fichier (par exemple, 'data/data.csv'): ")
            file_format = input("Entrez le format du fichier (csv/json): ").lower()
            if file_format in ['csv', 'json']:
                DataLoader.load_data(data_filter, file_path, file_format)
                print("Données chargées avec succès.")
            else:
                print("Format de fichier non valide. Veuillez entrer 'csv' ou 'json'.")
        elif choice == '2':
            file_path = input("Entrez le chemin pour sauvegarder le fichier (par exemple, 'data/output.csv'): ")
            file_format = input("Entrez le format du fichier (csv/json): ").lower()
            if file_format in ['csv', 'json']:
                DataSaver.save_data(data_filter, file_path, file_format)
                print(f"Données sauvegardées avec succès dans {file_path}.")
            else:
                print("Format de fichier non valide. Veuillez entrer 'csv' ou 'json'.")
        elif choice == '3':
            StatsCalculator.display_stats(data_filter)
        elif choice == '4':
            field = input("Entrez le nom du champ: ")
            operator = input("Entrez l'opérateur (==, !=, <, <=, >, >=): ")
            value = input("Entrez la valeur: ")
            if operator in ['==', '!=', '<', '<=', '>', '>=']:
                data_filter.filter_data(field, operator, value)
                print("Données filtrées.")
            else:
                print("Opérateur non valide. Veuillez entrer un des suivants: ==, !=, <, <=, >, >=.")
        elif choice == '5':
            field = input("Entrez le nom du champ pour le tri: ")
            reverse = input("Tri descendant? (o/n): ").lower() == 'o'
            DataSorter.sort_data(data_filter, field, reverse)
            print("Données triées.")
        elif choice == '6':
            DataDisplayer.display_data(data_filter)
        elif choice == '7':
            print("Fermeture du programme.")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
