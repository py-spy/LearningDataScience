## 2. Data cleaning ##

import pandas as pd
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
filtered_cars = cars[cars['horsepower'] != '?']
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype(float)

## 3. Data Exploration ##

import matplotlib.pyplot as plt
filtered_cars.plot('horsepower', 'mpg', kind='scatter', c='red')
filtered_cars.plot('weight', 'mpg', kind='scatter', c='blue')
plt.show()

## 4. Fitting a model ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(filtered_cars[['horsepower']], filtered_cars['mpg'])
predictions = lr.predict(filtered_cars[['horsepower']])
print(predictions[0:5])
print(filtered_cars['mpg'].values)

## 5. Plotting the predictions ##

import matplotlib.pyplot as plt
plt.scatter(filtered_cars['horsepower'], predictions, c = 'blue')
plt.scatter(filtered_cars['horsepower'], filtered_cars['mpg'], c = 'red')
plt.show()

## 6. Error metrics ##

from sklearn.metrics import mean_squared_error
from math import sqrt
mse = mean_squared_error(filtered_cars['mpg'], predictions)
rmse = sqrt(mse)
