import pandas as pd
import math as m
d={'day':[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
   'outlook':["sunny","sunny","overcast","rain","rain","rain","overcast","sunny","sunny","rain","sunny","overcast","overcast","rain"],
   'temp':["hot","hot","hot","mild","cool","cool","cool","mild","cool","mild","mild","mild","hot","mild"],
   'homidity':["high","high","high","high","normal","normal","normal","high","normal","normal","normal","high","normal","high"],
   'wind':["weak","strong","weak","weak","weak","strong","weak","weak","weak","strong","strong","strong","weak","strong"],
   'play tennis':["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"]}
df=pd.DataFrame(d)
print(df)
z=list(df['play tennis'])
x=z.count("yes")
print("number of yes:",x)
y=z.count("no")
print("number of no",y)
p=x/14
print("probability of yes:",p)
q=y/14
print("probability of no:",q)
c=m.log2(p)
print("log of probability yes:",c)
t=m.log2(q)
print("log of probability yes:",t)
E=-(p*c)-(q*t)
print(E)

