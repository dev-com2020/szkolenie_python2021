# uchwyt = open("plik.txt", "r", encoding="utf-8")

try:
    plik = open("plik.txt", "a", encoding="utf-8")
    try:
        plik.write("Test obsługi pliku")
    finally:
        print("Zamykam plik...")
        plik.close()
except ValueError:
    print("Brak pliku, albo zła %s nazwa?")

raise NameError('zła nazwa pliku')


