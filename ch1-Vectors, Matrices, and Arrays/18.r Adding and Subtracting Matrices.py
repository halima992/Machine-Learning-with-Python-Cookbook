# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:30:38 2021

@author: Halima
"""
# Load library
import numpy as np

# Create matrix
matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1], 
                     [1, 1, 2]])

# Ceatre matrix 
matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])

# Add two matrices
matrix_c = np.add(matrix_a,matrix_b)

# Subtract two matrices
matrix_d = np.subtract(matrix_a,matrix_b)