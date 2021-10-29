import pandas as pd

film = pd.read_csv('film.csv', sep=';', encoding="ISO-8859-1",
                   skiprows=[1], dtype={'Year':'int64','Length': 'float64', 'Popularity': 'float64'},
                   usecols=['Year', 'Length', 'Popularity', 'Awards'],
                   converters={'Awards': lambda x: True if x == 'Yes' else False})

# print(film.groupby('Year').count())
# print(film.groupby('Year').Popularity.mean())
# print(film.groupby(['Year','Awards']).Length.mean())

#print(film.groupby('Year').agg({'Popularity': ['min', 'max'], 'Length': ['min', 'max']}))
#print(film.groupby('Year').agg(minimalna_długość=('Length','min'),
#                               maksymalna_długość=('Length','max'),))

print(film[(film['Year'] > 1980) & (film['Year'] <= 1990)].groupby('Year').Length.mean())