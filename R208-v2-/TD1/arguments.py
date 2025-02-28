import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Aucun argument après le nom du script : {sys.argv[0]}")

    else:
        print(f" (base)   {sys.argv[0]}")

        for i in range(1, len(sys.argv)): # Boucle avec index…
            print(f"\t --> {sys.argv[i]}")