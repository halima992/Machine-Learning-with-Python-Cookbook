# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:38:37 2021

@author: Halima
"""
# Load library
import numpy as np

# Create matrix
matrix_a = np.array([[1, 1],
                     [1, 2]])

# Ceatre matrix 
matrix_b = np.array([[1, 3],
                     [1, 2]])

# Multiply two matrices
matrix_c = np.dot(matrix_a,matrix_b)

# Alternatively, in Python 3.5+ we can use the @ operator:
# Multiply two matrices
matrix_d = matrix_a @ matrix_b
