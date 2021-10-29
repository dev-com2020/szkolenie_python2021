import pandas as pd

miasta = pd.read_csv('worldcities.csv')

#print(miasta[0:5][['city']])
# print(miasta.head())
# print(miasta.tail())
wybrane = miasta[['city', 'capital', 'id']]
#print(miasta.shape)
#print(miasta.info())
#print(miasta.describe())
#print(miasta.population.describe())
#print(miasta.isnull().sum())
#print(miasta.notnull().sum())
#print(miasta.duplicated().sum())
#print(miasta.drop_duplicates())



