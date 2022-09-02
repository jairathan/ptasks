from cProfile import label
from ctypes import sizeof
from turtle import color, width
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:\\VsProjects\\python practice\\data sets\\Bengaluru_House_Data.csv')

df=df.fillna({'size': df['size'].mean})
df['society']=df['society'].fillna(method='pad')
df['location']=df['location'].fillna(method='pad')
df=df.fillna({'bath':df['bath'].mean})
df=df.fillna({'balcony':df['balcony'].mean})

print(df)

x=df['location'].iloc[0:10]
y=df['price'].iloc[0:10]
bar=plt.bar(x,  y,color='g',label='prices')
for i in range(len(bar)):
    bar[i].set_hatch('-')


plt.title('banglore areawise prices')
plt.xlabel('locations')
plt.ylabel('price')
plt.legend()
plt.xticks(list(df['location'].iloc[0:10]),size=4)
plt.show()

