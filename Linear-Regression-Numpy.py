# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 00:52:15 2019

@author: ibrahim mert oğurcu

"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv("linear.csv")  # Verimizi okuyalım

print(data) 

x = data["Square-meter"] 
y = data["price"] 
x = pd.DataFrame.as_matrix(x) 
y = pd.DataFrame.as_matrix(y)

print(x)
print(y) 

plt.scatter(x,y) 


m,b = np.polyfit(x,y,1)# NumPy bizim için grafiğe oturtuyor çizgimizi. Bunu matematiksel
# İşlemlerle uzun uzun da yapabilirdik. Fakat NumPy halihazırda sahip. Çok kafa karıştırmamak 
# Adına böylesi daha iyi.
# np.polyfit(x ekseni, y ekseni, kaçıncı dereceden polinom denklemi) ki biz birinci dereceden kullanacağız.


a = np.arange(150)

plt.scatter(x,y) 
plt.plot(m*a+b) 


z = int(input("How many square meters?"))
est = m*z+b
print(est)

plt.scatter(z,est,c="red",marker=">")

plt.show()
print("y=",m,"x+",b)