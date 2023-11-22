import uuid

class Equipement:
    

    def __init__(self, id, type, modele, numero_serie, date_acquisition, localisation, etat):
        self._id = str(uuid.uuid4())
        self._type = type
        self._modele = modele
        self._numero_serie = numero_serie
        self._date_acquisition = date_acquisition
        self._localisation = localisation
        self._etat = etat

        Equipement.equipements_instances.append(self)

    # Getters

    def get_id(self):
        return self._id
    
    def get_type(self):
        return self._type

    def get_modele(self):
        return self._modele

    def get_numero_serie(self):
        return self._numero_serie

    def get_date_acquisition(self):
        return self._date_acquisition

    def get_localisation(self):
        return self._localisation

    def get_etat(self):
        return self._etat

    # Setters
    def set_type(self, new_type):
        self._type = new_type

    def set_modele(self, new_modele):
        self._modele = new_modele

    def set_numero_serie(self, new_numero_serie):
        self._numero_serie = new_numero_serie

    def set_date_acquisition(self, new_date_acquisition):
        self._date_acquisition = new_date_acquisition

    def set_localisation(self, new_localisation):
        self._localisation = new_localisation

    def set_etat(self, new_etat):
        self._etat = new_etat

    equipements_instances = []
    
    @classmethod
    def get_all_instances(cls):
        return cls.equipements_instances




