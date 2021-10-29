import re
"""
Wyrażenie Opis
a | A   a lub A
.       jakikolwiek znak z wyjątkiem nowego wiersza
^       początek wiersza
$       koniec wiersza
*       0 lub więcej wystąpień poprzedzającego wyrażenia
+       1 lub więcej wystąpień poprzedzającego wyrażenia
?       0 lub 1 wystąpienie poprzedzającego wyrażenia
{n}     n wystąpień poprzedzającego wyrażenia
{m, n}  od m do n wystąpień poprzedzającego wyrażenia
\d      cyfra
\w      znak alfanumeryczny
\s      spacja, tabulator, znak końca linii/nowego wiersza

# """
# wyr = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
# wyr2 = "^((\d{3}[- ]\d{3}[- ]\d{2}[- ]\d{2})|(\d{3}[- ]\d{2}[- ]\d{2}[- ]\d{3}))$"
# wyr3 = "^\d{11}$"
# wyr4= "\d{2}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}[ ]\d{4}."
#
# tekst=input("Podaj tekst:")
#
# r = re.findall(wyr,tekst)
# print(r)

tekst = """Wyobraz sobie, ze ten tekst zawiera numer
PIN 9434 twojej karty do bankomatu, a ty wlasnie go
zapomniales. Jak szybko go odnalezc?"""

sciezka = r'\d\d\d\d'
dopasowanie = re.search(sciezka, tekst)

if dopasowanie: #Sprawdzamy czy udalo sie cos znalezc
    numer = dopasowanie.group()
    print(numer)
