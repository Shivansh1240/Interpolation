# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:08:50 2024

@author: Shivansh Mishra
"""

import numpy as np 
import pandas as pd 

data = np.loadtxt('ULL_1995_B.txt')


df = pd.DataFrame(data)
df.head()
print(df.head())
df.isnull().sum()
print(df.isnull().sum())

df_interpolated = df.interpolate()
df_interpolated.to_csv('interpolated_data.txt', sep='\t', index=False)



