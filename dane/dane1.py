import pandas as pd

# print(pd.read_excel('imiona.xlsx'))
# print(pd.read_csv('Halloween.csv'))

zbior = pd.DataFrame()
# print(zbior)

lista = [[1, 2, 5, 7], [11, 22, 55, 77], [33, 44, 55, 0]]

listanr1 = pd.DataFrame(lista)
listanr1.columns = ['Liczby_1', 'Liczby_2', 'Liczby_3', 'Liczby_4']
# print(listanr1)

slownik = {'Imie': ['Ania', 'Michał', 'Przemek'], 'Wiek': [18, 25, 40], 'Płeć': ['k', 'm', 'm']}
# print(pd.DataFrame(slownik))

s = pd.Series([11, 33, 55, 99])
#s = pd.Series(lista)
print(pd.DataFrame(s))

