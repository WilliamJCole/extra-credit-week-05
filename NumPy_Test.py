#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Using NumPy modules examples"""


import numpy as np


a = np.matrix('1 2; 3 4')
""" Creates a Matrix """
b = np.matrix('2 4; 5 6')

print (a)
print (b)

out1 = np.dot(a,b[, out])
""" Dot product of the matrices"""

print (out1)

out2 = np.linalg.matrix_power(a, 10)

print (out2)

cos = np.cos(1.5708[, out])
""" Cosine(1.5708rad)"""
print (cos)
