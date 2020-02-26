import numpy as np 
import pandas as pd 

#Question 1
series = pd.Series([7,11,13,17])
print(series)
#Question 2
arry = pd.Series(100, range(5))
print (arry)
#Question 3
random20= pd.Series(np.random.randint(0,high=100, size=20))
randescribe = random20.describe()
print(randescribe)
Question 4
temperatures = pd.Series([98.6,98.9,100.2,97.9],index =['Julie','Charlie','Sam','Andrea'])
print(temperatures)
#Question 5
dictionary = {'Julie':98.6,'Charlie':98.9,'Sam':100.2,'Andrea':97.9}
temperatures =pd.Series(dictionary)
print(temperatures)