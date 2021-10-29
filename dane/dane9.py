import pandas as pd
import sqlite3 as sql

film = pd.read_csv('film.csv', sep=';', encoding="ISO-8859-1",
                   skiprows=[1], dtype={'Year': 'int64', 'Length': 'float64', 'Popularity': 'float64'},
                   usecols=['Year', 'Length', 'Popularity', 'Awards'],
                   converters={'Awards': lambda x: True if x == 'Yes' else False})



conn = sql.connect('new.sqlite')
#film.to_sql('filmy',conn)

movies = pd.read_sql("select * from filmy where Year > 1995",conn)
print(movies)

