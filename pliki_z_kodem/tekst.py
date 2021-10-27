# artykul = """
#             *** Mój program ***
#                autor: Comarch
#         ...Tu będzie mój program...
#         - a tu będzie menu...
#
#
# """
# print(artykul)
#
# tekst = "Tomasz"
# firma = "Comarch"
#
# print(tekst[0]) # pierwszy
# print(tekst[-1]) # ostatni
# print(tekst[0] + tekst[-2] + tekst[1:3])
# print(tekst + firma[3:])
#
# print(firma.lower().count("c"))
# print(firma.upper().count("C"))
#
# print(len(firma))

imie = "Tomasz"
wiek = 38
print("mam na imię %s" % imie)
print("cześć, jestem %s, mieszkam w Kielcach. Mam %i lat" % (imie, wiek))

x = 45.564983275698234792348

print("Liczba komet w okolicy księżyca = %.1f" % x)
print(f"mam na imię {imie}")

print("Lubię %(jezyk)s" % {"jezyk": "Pythona"})
print("Lubię język {0} oraz {1}".format("Java","Python"))

# %s = string
# %i = integer
# %f = float
# %x lub %X - liczba szesnastkowa