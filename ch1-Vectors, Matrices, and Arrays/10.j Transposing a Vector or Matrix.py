# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:56:09 2021

@author: Halima
"""
# Load library
import numpy as np

#create matrix 
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
# Transpose matrix
transpose_matrix = matrix.T

# =============================================================================
# Transpose vector
# =============================================================================
transpose_vector = np.array([1,2,3,4,5,6,7,8]).T #vector cannot transpose becuse it is collection of values 

# =============================================================================
# Transpose row vector
# =============================================================================
transpose_row_vector = np.array([[1,2,3,4,5,6,7,8]]).T #row vector become column vector 