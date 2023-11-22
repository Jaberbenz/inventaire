from equipement import Equipement
import uuid
import csv

class Inventaire:
    def __init__(self, classe_equipement, csv_file_path):
        self.classe_equipement = classe_equipement
        self.csv_file_path = csv_file_path
        self.equipements_instances = self.charger_equipements_de_csv()

    def charger_equipements_de_csv(self):
        equipements = []
        try:
            with open(self.csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    equipement = self.classe_equipement(
                        row['ID'], row['Type'], row['Modèle'], row['Numéro de série'],
                        row['Date d\'acquisition'], row['Localisation'], row['État']
                    )
                    equipements.append(equipement)
        except FileNotFoundError:
            print(f"Le fichier CSV {self.csv_file_path} n'existe pas. Un nouveau fichier sera créé.")

        return equipements

    def sauvegarder_equipements_en_csv(self):
        with open(self.csv_file_path, mode='w', newline='') as file:
            fieldnames = ['ID', 'Type', 'Modèle', 'Numéro de série', 'Date d\'acquisition', 'Localisation', 'État']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Écrire l'en-tête
            writer.writeheader()

            # Écrire les données pour chaque équipement
            for equipement in self.equipements_instances:
                writer.writerow({
                    'ID': equipement._id,
                    'Type': equipement._type,
                    'Modèle': equipement._modele,
                    'Numéro de série': equipement._numero_serie,
                    'Date d\'acquisition': equipement._date_acquisition,
                    'Localisation': equipement._localisation,
                    'État': equipement._etat
                })

    def afficher_equipements(self):
        for equipement in self.equipements_instances:
            print(f"ID: {equipement._id}, Type: {equipement._type}, Modèle: {equipement._modele}")

    def ajouter_equipement(self, equipement):
        self.equipements_instances.append(equipement)
        self.sauvegarder_equipements_en_csv()

    def supprimer_equipement(self, equipement_id):
        equipement = self.trouver_equipement_par_id(equipement_id)
        if equipement:
            self.equipements_instances.remove(equipement)
            self.sauvegarder_equipements_en_csv()
            print(f"Équipement avec l'ID {equipement_id} supprimé de l'inventaire.")
        else:
            print(f"Aucun équipement trouvé avec l'ID {equipement_id}.")

    def modifier_equipement(self, equipement_id, new_type=None, new_modele=None, new_numero_serie=None,
                            new_date_acquisition=None, new_localisation=None, new_etat=None):
        equipement = self.trouver_equipement_par_id(equipement_id)
        if equipement:
            # Modifier les attributs de l'équipement
            if new_type is not None:
                equipement._type = new_type
            if new_modele is not None:
                equipement._modele = new_modele
            if new_numero_serie is not None:
                equipement._numero_serie = new_numero_serie
            if new_date_acquisition is not None:
                equipement._date_acquisition = new_date_acquisition
            if new_localisation is not None:
                equipement._localisation = new_localisation
            if new_etat is not None:
                equipement._etat = new_etat

            self.sauvegarder_equipements_en_csv()
            print(f"Équipement avec l'ID {equipement_id} modifié.")
        else:
            print(f"Aucun équipement trouvé avec l'ID {equipement_id}.")

    def trouver_equipement_par_id(self, equipement_id):
        for equipement in self.equipements_instances:
            if equipement._id == equipement_id:
                return equipement
        return None



# Exemple d'utilisation
csv_file_path = 'utils/equipements.csv'
inventaire = Inventaire(Equipement, csv_file_path)

# Afficher l'inventaire initial
print("Inventaire initial:")
inventaire.afficher_equipements()

# Ajouter un nouvel équipement à l'inventaire
nouvel_equipement = Equipement(str(uuid.uuid4()), "ordi", "lenovo", "67890", "2021-02-01", "bureau", "Indisponible")
inventaire.ajouter_equipement(nouvel_equipement)

# Afficher l'inventaire après l'ajout
print("\nInventaire après ajout:")
inventaire.afficher_equipements()

# Supprimer un équipement de l'inventaire
inventaire.supprimer_equipement(nouvel_equipement._id)

# Afficher l'inventaire après la suppression
print("\nInventaire après suppression:")
inventaire.afficher_equipements()
































