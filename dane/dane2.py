import pandas as pd

imiona = pd.read_excel('imiona.xlsx')

# print(pd.read_excel('imiona.xlsx',sheet_name='Wynik', header=1))

print(pd.read_excel('imiona.xlsx', sheet_name='Wynik2', header=None, names=['Imię', 'Nazwisko', 'Wynik']))
