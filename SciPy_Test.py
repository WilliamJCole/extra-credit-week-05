#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" Testing SciPy """


import scipy.integrate as integrate
import scipy.special as special
from scipy.optimize import minimize
import numpy as np

result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
""" integrates I=∫4.50J2.5(x)dx. """

print (result)

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rozen, x0, method='nelder-mead',
                options={'xtol': 1e-8, 'disp': True})
""" Examples of miminization of an array using the nelder-mead
algorithm"""

print (res)
