
# licznik = 0
# while True:
#     licznik += 1
#     print(licznik)
#     if licznik > 10:
#         break


lista = []
print("Podaj liczby...")
print("Wpisz '000' aby zakończyć...")
while True:
    wejscie = input()
    if wejscie == 'stop':
        break
    lista.append(int(wejscie))
print("Twoja lista: ",lista)