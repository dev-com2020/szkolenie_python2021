# matplotlib inline

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
x = df['date']
y = df['Close']

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y)
plt.show()