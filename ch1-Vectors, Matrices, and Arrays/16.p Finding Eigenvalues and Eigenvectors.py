# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:15:38 2021

@author: Halima
"""
# Load library
import numpy as np

# Create matrix
matrix = np.array([[1, -1, 3], 
                   [1, 1, 6], 
                   [3, 8, 9]])
# Calculate eigenvalues and eigenvectors 
eigenvalues, eigenvectors = np.linalg.eig(matrix)
