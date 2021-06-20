# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:03:54 2021

@author: Halima
"""
# Load library
import numpy as np 

# Create matrix
matrix= np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
# Return mean
mean = np.mean(matrix)
# Return variance
variance= np.var(matrix)
# Return standard deviation
standard = np.std(matrix)

# Find the mean value in each column
print(np.mean(matrix, axis=0))