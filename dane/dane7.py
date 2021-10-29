import pandas as pd

#
# def zamien(wartosc):
#     if wartosc == 'No':
#         return False
#     if wartosc == 'Yes':
#         return True


film = pd.read_csv('film.csv', sep=';', encoding="ISO-8859-1",
                   skiprows=[1], dtype={'Length': 'float64', 'Popularity': 'float64'},
                   converters={'Awards': lambda x: True if x == 'Yes' else False})

# film = film.drop(0)
film = film.drop(columns=['*Image'])

# film.Awards = film.Awards.apply(zamien)

# film.Length = pd.to_numeric(film.Length)
# film.Length = film.Length.astype('float64')
# print(film.info())
# print(film.Length.mean())
print(film)
