# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 08:37:33 2021

@author: Halima
"""
# Load library import numpy as np
import numpy as np
# Create matrix 
matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
# Create function that adds 100 to something 
add_100 = lambda i: i+100
# Create vectorized function
vectorized_add_100 = np.vectorize(add_100)
# Apply function to all elements in matrix
print(vectorized_add_100(matrix))

# another way is broadcasting
#Add 100 to all elements 
matrix = matrix + 100
