from pathlib import Path
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 4:
        print(f"Moins de 4 argumnets fournis après :  {sys.argv[0]}")

    else:
        print(f" sys.argv[0]")
        fichier = sys.argv[1]
        f_path = Path(fichier)
        f_path = f_path.resolve()
        nom = sys.argv[2].upper()
        prenom =  sys.argv[3].capitalize()
        notes = sys.argv[4:]

        total = 0.0
        for note in notes:
            total += float(note)
        moyenne = total / len(notes)

