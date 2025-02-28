from obj_voitures import Voitures

voiture19 = Voitures()
print(voiture19)

clio = Voitures(marque = "Renault", modele = "Captur_TCE_90ch", conso = 7.2, couleur = "Gris foncé", prix = 20000)  # Création d’une instance.
captur = Voitures(marque = "Renault", modele = "Clio_TCE_100ch", conso = 5.5, couleur = "Bleu nuit", prix = 17000)  # Création d’une instance.

print(clio)
print(captur)

distance = 1060
calcul_clio = clio.calcul_consommation(distance)
print(f'Pour la clio', calcul_clio)
calcul_captur = captur.calcul_consommation(distance)
print(f'Pour la captur', calcul_captur)

modif_prix_litre = 1.70     #float(input('Veuillez entrer le prix du litre : '))

calcul_prix_clio = clio.calcul_prix(modif_prix_litre)
print(f'Le prix du carburant pour la clio est : ', calcul_prix_clio, '€')
calcul_prix_captur = captur.calcul_prix(modif_prix_litre)
print(f'Le prix du carburant pour la clio est : ', calcul_prix_captur, '€')

print(f'Lémisson de CO2 de la clio est de : ', Voitures.calcul_co2(clio, distance), 'Kg')
print(f'Lémisson de CO2 de la clio est de : ', Voitures.calcul_co2(captur, distance), 'Kg')