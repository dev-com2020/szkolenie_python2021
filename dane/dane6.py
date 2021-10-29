import pandas as pd

df = pd.DataFrame({'Osoba': ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
                   'Wynik': [15, 38, 21]})

def sprawdz(punkty):
    if punkty > 20:
        return 'Zdany'
    else:
        return 'Oblany'

def rozdziel(wiersz):
    wiersz['Imię'],wiersz['Nazwisko'] = wiersz['Osoba'].split(" ")
    return wiersz


df.Wynik = df.Wynik.apply(sprawdz)
df = df.apply(rozdziel, axis=1)
print(df)

"""
Typ danych w Python Pandas DataFrame	Odpowiednik w Python
object	                                String (łańcuch znaków)
int64	                                Integer (liczba całkowita)
float64	                                Float (liczba rzeczywiste)
bool	                                bool (True lub False)
Category	                            NA
datetime	                            datetime

"""