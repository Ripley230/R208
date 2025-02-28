class Voitures():
    # Constructeur avec 3 arguments...
    def __init__(self, marque = "Ferrari", modele = "SF90_spider", annee = 2010) :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"

car = Voitures("Renault", "Clio", 2018) # Création d’une instance.
caisse = car.modele # Lecture d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !") # Affichage.
car.annee = 2020 # Ecriture (modification) d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")

print(car)

ma_voiture = Voitures("Bugatti", "Veyron")
print(ma_voiture)

voiture4 = Voitures()
print(voiture4)

voiture5 = Voitures("F40")
print(voiture5)

voiture6 = Voitures(modele = "296_GTS")
print(voiture6)

print(type(voiture6))
print(vars(voiture6))
print(dir(voiture6))