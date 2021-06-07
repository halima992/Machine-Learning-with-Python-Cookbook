# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:32:47 2021

@author: Halima
"""

# Load library 
import numpy as np
# Create row vector 
vector = np.array([1, 2, 3, 4, 5, 6])
# Create matrix 
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Select third element of vector 
print(vector[2])
# Select second row, second column 
print(matrix[1,1])
print('-'*20)

# Discussion
# Select all elements of a vector 
print(vector[:])
print('-'*20)
#------------------------------------------------------------------------------
# Select everything up to and including the third element 
print(vector[:3])
print('-'*20)
#------------------------------------------------------------------------------
# Select everything after the third element 
print(vector[3:])
print('-'*20)
#------------------------------------------------------------------------------
# Select the last element 
print(vector[-1])
print('-'*20)
#------------------------------------------------------------------------------
# Select the first two rows and all columns of a matrix 
print(matrix[:2,:])
print('-'*20)
#------------------------------------------------------------------------------
# Select all rows and the second column
print(matrix[:,1:2])