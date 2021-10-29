import pandas as pd

miasta = pd.read_csv('worldcities.csv')

miasta.to_excel("wynik_miasta.xlsx", sheet_name='miasta')
miasta.to_json("wynik_miasta_2.json")
