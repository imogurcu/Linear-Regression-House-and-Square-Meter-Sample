# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:11:43 2019

@author: ibrahim mert oğurcu
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt

data = pd.read_csv("linear.csv")

x = data["Square-meter"]
y = data["price"]


x = x.values.reshape(99,1)
y = y.values.reshape(99,1)


linearRegression = lr() # Call the linear regression

linearRegression.fit(x,y) 

linearRegression.predict(x) #x'e göre, yani metrekareye göre ev fiyatlarını tahmin edeceğiz.

m = linearRegression.coef_ # Coefficient - yani katsayı, bu komutla eğimimizi
                          # Yani m i buluyoruz.
b = linearRegression.intercept_ # Intercept - b dir. yani y = mx+b 'de x'e sıfır 
                              # verdiğimizde kalan değer.

a = np.arange(150)

plt.scatter(x,y) 
plt.scatter(a,m*a+b, c="red",marker=">")
plt.show()



print('Slope: ', linearRegression.coef_)
print('Intersection Y: ', linearRegression.intercept_)


print("Equation")
print("y=",m,"x+",b)
