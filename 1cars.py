import pandas as pd
cars=pd.read_csv('cars.csv')
Firstfive=cars.head()
a=Firstfive.iloc[:,1:12:2]
b=cars[cars['Model']=='Mazda RX4']
c=cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
d=cars.loc[(cars['Model']=='Mazda RX4 Wag')|(cars['Model']=='Ford Pantera L')|(cars['Model']=='Honda Civic'),['Model','cyl','gear']]
print(a)
print(b)
print(c)
print(d)