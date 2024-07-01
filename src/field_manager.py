from utils.type_converter import auto_convert

class FieldManager:
    @staticmethod
    def manage_fields(data_filter):
        while True:
            print("\nGestion des champs:")
            print("1. Ajouter un champ")
            print("2. Retirer un champ")
            print("3. Retour au menu principal")

            choice = input("Choisissez une option: ")

            if choice == '1':
                field_name = input("Entrez le nom du nouveau champ: ")
                default_value = input("Entrez la valeur par défaut pour ce champ: ")
                for item in data_filter.data:
                    item[field_name] = auto_convert(default_value)
                print(f"Champ '{field_name}' ajouté avec succès.")

            elif choice == '2':
                field_name = input("Entrez le nom du champ à retirer: ")
                if data_filter.data and field_name in data_filter.data[0]:
                    for item in data_filter.data:
                        item.pop(field_name, None)
                    print(f"Champ '{field_name}' retiré avec succès.")
                else:
                    print(f"Le champ '{field_name}' n'existe pas.")

            elif choice == '3':
                break

            else:
                print("Option invalide. Veuillez réessayer.")