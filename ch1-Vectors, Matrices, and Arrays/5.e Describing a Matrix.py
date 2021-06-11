# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 08:24:54 2021

@author: Halima
"""
# Load library 
import numpy as np
# Create matrix 
matrix = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
# View number of rows and columns
print(matrix.shape)
# View number of elements (rows * columns)
print(matrix.size)
# View number of dimensions
print(matrix.ndim)