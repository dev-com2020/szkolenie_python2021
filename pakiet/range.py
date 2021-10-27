# liczby = range(5)
# print(liczby)
#
# for i in range(5): #stop
#     print(i)
#
# for i in range(1, 10):  # start,stop
#     print(i)
#
# for i in range(1, 10, 2):  # start,stop, step
#     print(i)
#
# for i in range(-10, 10):  # start,stop
#     print(i)
#
# for i in range(-10, 10, 2):  # start,stop,step
#     print(i)
#
# for i in range(-5, -10, -2):  # start,stop,step
#     print(i)

# tekst = "Kurs programowania w języku Python dla nieprogramistów"
# licznik = 0
#
# for znak in tekst:
#     if znak == 'P' or znak == 'p':
#         licznik += 1
# print("Litera p wystąpiła: ", licznik, "razy.")

# liczba = int(input("Podaj liczbę: "))
# cyfry = [1, 3, 5, 7, 9]
#
# if liczba in cyfry:
#     print("Liczba jest w zbiorze!")

# if liczba < 10:
#     print("jest to mała liczba!")
# elif 9 < liczba < 100:
#     print("to już duża liczba, ale mniejsza od 100")
# else:
#     print("To jest liczba powyżej 100")

# nic = None #odpowiednik Null
# pusty_string = ""
#
# if not nic:
#     print("None to Null i False")
# if not pusty_string:
#     print("Pusty string to False")
# if nic == pusty_string:
#     print("None i pusty string to False")
# if pusty_string == "":
#     print("To jest pusty string")


def zasieg():
    slownik = {"imie": "Marek", "nazwisko": "Kowalski", "plec": "mezczyzna"}

    for key in slownik:
        print(key)

    for val in slownik.values():
        print(val)

    for key,values in slownik.items():
        print(key + " -> " + values)