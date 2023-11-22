from interface.gestion_inventaire import GestionInventaireApp
from gestion_dinventaire.inventaire import Inventaire

def main():
    # Initialisation de l'interface utilisateur
    interface = GestionInventaireApp()

    # Initialisation de la gestion d'inventaire
    gestion_inventaire = Inventaire()

    # Lier l'interface et la gestion d'inventaire
    interface.set_gestion_inventaire(gestion_inventaire)

    # Démarrer l'interface utilisateur
    interface.run()

if __name__ == "__main__":
    main()
