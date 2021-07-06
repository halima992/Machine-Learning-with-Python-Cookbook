# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:14:32 2021

@author: Halima
"""
# Load library 
import numpy as np
# Create matrix
matrix = np.array([[1,2,3],
                   [2,4,6],
                   [3,8,9]])

# Return determinant of matrix
matrix_determinant = np.linalg.det(matrix)
