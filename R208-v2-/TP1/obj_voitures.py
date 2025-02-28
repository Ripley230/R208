import base64

class Voitures():
    prix_litre = 1.70
    # Constructeur avec 3 arguments...
    def __init__(self, marque = "Ferrari", modele = "SF90_spider", annee = 2010, prix = None, couleur = "Blanc", conso = 6.0, _id_serie = "A123 B456 C789",  __audio_code = "0000 ") :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso
        self._id_serie = base64.b64encode(_id_serie.encode()).decode()
        self.__audio_code = base64.b64encode(__audio_code.encode()).decode()

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Voiture : {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso}/100Km - {self.prix}€ - {self._id_serie} - {self.__audio_code}"

    def calcul_consommation(self, distance):
        return self.conso*distance/100

    def calcul_prix(self, prix_litre):
        return self.conso*prix_litre

    def calcul_co2(self, conso_co2):
        return self.calcul_consommation(conso_co2)*2.3