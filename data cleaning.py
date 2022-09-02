import pandas as pd

df=pd.read_csv('C:\\VsProjects\\python practice\\data sets\\Bengaluru_House_Data.csv')

df=df.fillna({'size': df['size'].mean})
df['society']=df['society'].fillna(method='pad')
df['location']=df['location'].fillna(method='pad')
df=df.fillna({'bath':df['bath'].mean})
df=df.fillna({'balcony':df['balcony'].mean})
print(df.isnull().sum())