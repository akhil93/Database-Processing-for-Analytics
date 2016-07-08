# -*- coding: utf-8 -*-
"""
Created on Sat Nov 01 20:00:18 2014

@author: Akhilkumar
"""
import numpy as np
def ORFunction(x,y):
    new_matrix = []
    if len(x) == len(y):
        a = [0,1]
        b = [0,1]
        for i in a:
            for j in b:
                ind =  x[i][j] or y[i][j]
                new_matrix.append(ind)
                New_Matrix = np.asmatrix(new_matrix)
    Mat_Shape=np.resize(New_Matrix,(2,2))
    print Mat_Shape
