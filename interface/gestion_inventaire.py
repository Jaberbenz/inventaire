# tkinter_app.py

import tkinter as tk

from gestion_dinventaire.equipement import Equipement
from gestion_dinventaire.inventaire import Inventaire

class App:
    def __init__(self, root, inventaire):
        self.root = root
        self.inventaire = inventaire
        self.setup_ui()

    def setup_ui(self):
        # Créez ici votre interface graphique avec Tkinter
        # Utilisez self.inventaire pour accéder aux équipements et effectuer des opérations

        # Exemple minimal :
        label = tk.Label(self.root, text="Inventaire d'équipements")
        label.pack()

        for equipement in self.inventaire.equipements_instances:
            entry = tk.Entry(self.root, text=f"{equipement._id}: {equipement._type} - {equipement._modele}")
            entry.pack()

if __name__ == "__main__":
    csv_file_path = 'equipements.csv'
    inventaire = Inventaire(Equipement, csv_file_path)

    root = tk.Tk()
    app = App(root, inventaire)
    root.mainloop()
