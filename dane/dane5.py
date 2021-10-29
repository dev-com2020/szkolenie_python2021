import pandas as pd

kostium = pd.read_csv('Halloween.csv', header=2)
# print(kostium.head())
kostium['Nowa'] = '0'
kostium.loc[kostium['1'] == "Rabbit", 'Nowa'] = "X"
#print(kostium.rename(columns={'1': 'Pierwszy', '2': 'Drugi'}))
#print(kostium.drop('Nowa', axis=1))
kostium['Połączone'] = kostium['2'] + ' | ' + kostium['3']
kostium[['Trzeci',"Czwarty"]] = kostium.Połączone.str.split('|', expand=True)
print(kostium)

# kostium[3:4]['1'] = "Batman" # tak się nie da :(

# print(kostium.index)
# print(kostium.region.is_unique)
# kostium.set_index('region', inplace=True)
# kostium.reset_index(inplace=True)
# kostium.loc['Florida', '1'] = "Batman"

# print(kostium.iloc[9, 1])
# print(kostium.loc['Florida'][['1', '2', '3', '4', '5']])
# print(kostium)

# for index, zawartosc in kostium.iterrows():
#     if zawartosc['1'] == 'Rabbit':
#         print(zawartosc['region'])

# print(kostium[(kostium['1'] == 'Rabbit') | (kostium['1'] == 'Batman')])
# print(kostium[(kostium['1'] == 'Rabbit') & (kostium['2'] == 'Clown')])
