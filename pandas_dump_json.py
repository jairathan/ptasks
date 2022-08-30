from operator import index
import pandas as pd
import json
df = pd.read_csv('C:\\Users\\HP\\OneDrive\\Documents\\final_annotations.csv')

df = df.drop(['Unnamed: 0'], axis=1)
cols = list(df.columns)
g = df.groupby(['img_name'])

d = {}
for i, r in g:

    cols = list(r.columns)
    k = r[cols[1:]]
    c = {}
    for j in k:
        l = []
        for i in r[j]:
            l.append(i)
            c[j] = l

for i, r in g:
    d[i] = c

print(d)
x = str(d)

with open('nnn.json', 'w') as f:
    json.dump(x, f)
