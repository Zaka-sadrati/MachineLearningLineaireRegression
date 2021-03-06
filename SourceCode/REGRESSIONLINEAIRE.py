# -*- coding: utf-8 -*-

#importer le data set (utilise bibliothéque  pandas ) :
import pandas as pd
data=pd.read_csv("C:/Users/ki/Desktop/REGRESSIONLINEAIRE/DataSets/univariate_linear_regression_dataset.csv")

#séparation de données en deux variabe X & Y :
X = data.iloc[0:len(data),0]
Y = data.iloc[0:len(data),1]

#visualisation des données : 

import matplotlib.pyplot as plt 
axes = plt.axes()
axes.grid()
plt.scatter(X,Y)
plt.show()


#Applique l’algorithme :

from scipy import stats 

slope , intercept , r_value ,p_value , str_err = stats.linregress(X,Y)

def predict(X):
  return slope*X + intercept 
   
fitline=predict(X) 
plt.plot(X, fitline, c='r') 
plt.grid()
plt.scatter(X,Y)

#exemple de test : X=[0.25]
print("entree un nombre entre 0 et 25 :")
var = input("X= " )
var2 =int(var)
print("la valeur de Y pour F({}) est : {}".format(var2, predict(var2)))  