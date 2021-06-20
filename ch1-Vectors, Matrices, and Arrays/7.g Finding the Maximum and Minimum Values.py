# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:09:50 2021

@author: Halima
"""
# Load library
import numpy as np
# Create matrix
matrix = np.array([[1,2,3],
                   [4,5,6],
                  [7,8,9]])
# Return maximum element
print(np.max(matrix))
# Return minimum element
print(np.min(matrix))

# Find maximum element in each column
print(np.max(matrix,axis=0))
# Find maximum element in each row
print(np.min(matrix,axis=1))