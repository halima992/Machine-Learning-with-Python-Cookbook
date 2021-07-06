# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:22:10 2021

@author: Halima
"""
# Load library 
import numpy as np
# Create matrix
matrix = np.array([[1,2,3],
                   [7,9,8],
                   [1,2,0]])

# Return matrix rank
matrix_rank = np.linalg.matrix_rank(matrix)

