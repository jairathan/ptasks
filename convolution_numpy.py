import numpy as np

a=[1,2,3]
b=[2,3,4]
c=[3,4,5]
t=np.array([a,b,c])

d=[2,3,4,5,6]
e=[3,4,5,6,7]
f=[2,3,4,5,6]
g=[1,2,3,4,5]
h=[3,4,5,6,7]
z=[]


k=np.array([d,e,f,g,h])
for i in range(3):
    for j in range(3):
        m=np.sum(k[i:i+3,j:j+3]*t)
        z.append(m)
print(z)
k=np.array([z])

ww=k.reshape(3,3)

print(ww)
            








