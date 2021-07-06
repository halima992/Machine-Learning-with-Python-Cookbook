# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:46:19 2021

@author: Halima
"""
# Load library 
import numpy as np

# Create matrix 
matrix = np.array([[1, 4], 
                   [2, 5]])

# Calculate inverse of matrix 
np.linalg.inv(matrix)

# Multiply matrix and its inverse 
matrix_i = matrix @ np.linalg.inv(matrix)
