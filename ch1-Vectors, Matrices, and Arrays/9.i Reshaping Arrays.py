# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:20:59 2021

@author: Halima
"""

# Load library
import numpy as np  

#create matrix 
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12]])
size1 = matrix.size

# =============================================================================
# Reshape matrix into 2x6 matrix
# note: size matrix = size matrix2
# =============================================================================
matrix2 = matrix.reshape(2,6)
size2 = matrix2.size

# =============================================================================
# argument in reshape is -1 means “as many as needed”
# =============================================================================
matrix3 = matrix.reshape(1,-1) # one row and 12 column
matrix4 = matrix.reshape(3,-1) # 3 row and 4 column
matrix5 = matrix.reshape(-1,1) # 12 row and 1 column
matrix6 = matrix.reshape(12)   # will return a 1D array of that length


