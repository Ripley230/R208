import random

x = random.randint(10, 20)
liste_nombres = []

for i in range (x):
    y = random.randint(0, 100)
    liste_nombres.append(y)

while True:
    try:
        a = int(input(f"Donner une valeur d'index, en l'ocurence inférieur à {x} : "))
        if 0 <= a < x:
            print(f"La valeur qui correspond à l'index {a} est : {liste_nombres[a]}")
        else:
            print("La valeur saisie nexiste pas")

        z = int(input("Entrez un second nombre : "))
        valeur_finale = liste_nombres[a] / z
        print(f"La valeur finale obtenu est égale à {valeur_finale}")

    except IndexError:
        print("Veuillez entrer une valeur valide")
    except ValueError:
        print("Veuillez entrer un nombre et non un caractère")
    except ZeroDivisionError:
        print("On ne peux pas diviser par 0")