import pandas as pd
cars=pd.read_csv('cars.csv')
Firstfive=cars.head()
Lastfive=cars.tail()
print('Specs of the first five cars',Firstfive)
print('Specs of the last five cars',Lastfive)