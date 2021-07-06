# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:51:59 2021

@author: Halima
"""
# Load library 
import numpy as np
# Create matrix
matrix = np.matrix([[1,2,3],
                   [2,4,6],
                   [3,8,9]])
#return trace
trace = matrix.trace()
print(sum(matrix.diagonal()))
print(matrix.diagonal().sum())