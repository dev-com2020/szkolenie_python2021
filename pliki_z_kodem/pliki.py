# uchwyt = open("plik.txt", "r", encoding="utf-8")

try:
    with open("plik.txt", "r", encoding="utf-8") as plik:
        for linia in plik:
            print(linia, end="")
except IOError:
    print("Brak pliku, albo zła nazwa?")

