import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vehicles.csv')

df.drop(['id', 'url', 'region_url', 'image_url', 'description', 'county', 'lat', 'long', 'VIN', ], axis=1, inplace=True)

df['drive'].fillna('fwd', inplace=True)

df.drop(columns=['size'], inplace=True)

#replace the missing values in the 'paint_color' column with 'white'
df['paint_color'].fillna('white', inplace=True)

#replace the missing values in the 'cylinders' column with 4
df['cylinders'].fillna('4 cylinders', inplace=True)

df.drop(columns=['condition', 'type'], inplace=True)

#fill with mode in 'title_status'
df['title_status'].fillna(df['title_status'].mode()[0], inplace=True)

#fill with mode in 'fuel'
df['fuel'].fillna(df['fuel'].mode()[0], inplace=True)

#remplir l'odometer with the mean
df['odometer'].fillna(df['odometer'].mean(), inplace=True)
#change the 'other' with 'rotatry engine' if fuel is other else rotary engine
df.loc[(df['cylinders'] == 'other') & (df['fuel'] == 'other'), 'cylinders'] = 'rotary engine'

#change 'other' in fuel to gas, voir commd df[df['fuel'] == 'other']
df['fuel'].replace('other', 'gas', inplace=True)



below_500 = df[df['price'] < 500] #500$ ou 5000dh a reasonable price for a broken or a low car
len(below_500)

above = df[df['price'] > 200000] #200000dh is a reasonable price for a high spec car
len(above)
len(above)*100/len(df)


#drop the rows with price below 500 and above 200000
df = df[(df['price'] >= 500) & (df['price'] <= 200000)]
#reset the index
df.reset_index(drop=True, inplace=True)


# #classements et aggrégations selon différentes colonnes

# aggregation interressantes:
#     analyse selon les regions
#     analyse selon fuel
#     analyse selon le drive train
#

df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)


df.groupby('fuel')['price'].mean().sort_values(ascending=False)

df.groupby('drive')['price'].mean().sort_values(ascending=False)

df.groupby('region')['price'].mean().sort_values(ascending=False).head(10)

df[['odometer', 'price']].plot.scatter(x='odometer', y='price', alpha=0.5)

df['price_per_km'] = df['price'] / df['odometer']
df.groupby('fuel')['price_per_km'].mean().sort_values(ascending=False)

df.groupby(['drive', 'fuel'])['price'].mean().sort_values(ascending=False)

