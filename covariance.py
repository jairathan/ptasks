import numpy as np
a=[2,3,4]
b=[3,4,5]
c=[3,6,7]


e=np.array([a,b,c])

sum=0
for i in e[:,0:1]:
    sum=sum+i

m1=sum/len(e[:,0:1])


sum0=0
for i in e[:,1:2]:
    sum0=sum0+i

m2=sum0/len(e[:,1:2])

sum1=0
for i in e[:,2:3]:
    sum1=sum1+i

m3=sum1/len(e[:,2:3])

t1=[]
for i in e[:,0:1]:
    dif=i-m1
    t1.append(dif)
    
        
t2=[]
for i in e[:,1:2]:
    dif=i-m2
    t2.append(dif)
    
t3=[]
for i in e[:,2:3]:
    dif=i-m3
    t3.append(dif)
    

newm=np.array([t1,t2,t3])

print(e)
pp=newm.reshape(3,3)

covar=pp.T
print(covar)

