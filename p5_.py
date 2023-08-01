import pandas as pd 
import numpy as np 
df = pd.DataFrame([[10, np.nan, 30, 40], [7, 14, 21, 28], [55, np.nan, 8, 12], 
[15, 14, np.nan, 8], [7, 1, 1, np.nan], [np.nan, 4, 9, 2]], 
columns=['Apple', 'Orange', 'Banana', 'Pear'], 
index=['Basket1', 'Basket2', 'Basket3', 'Basket4','Basket5', 'Basket6']) 
print("Input:")
print(df) 
print("\nOutput:")
#print("By Prithvi Vasta")
df.fillna(df.mean())
