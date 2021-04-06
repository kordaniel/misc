#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:13:41 2021

@author: siipola

https://en.wikipedia.org/wiki/Newton%27s_method
https://en.wikipedia.org/wiki/Numerical_differentiation
https://en.wikipedia.org/wiki/Spline_(mathematics)
https://www.tutorialspoint.com/scipy/scipy_interpolate.htm

Algorithm explained:
    
1: Form a set of points (x) with numpy linspace.
2: Calculate the function f at these points.
3: Calculate the derivative of the function f at these points.
4: Form a spline using the calculated derivative points.
5: Using Newton's method, calculate the root of the derivative function.
    - Root is a point where the function is zero.
    - As the root of the derivative function is found, we know the minimum 
        point of our function.
6: Print the result.


"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import sys


""" Initialize the parameters of the model. """
N = 100
startPoint = 0
endPoint = 4
h = 1e-6
targetAccuracy = 1e-6
currentBest = 1e10
test = True
iterationRoundsMax = 100 
iterations = 0
foundMinimumPoint = False


x = np.linspace(startPoint, endPoint, N)
fx = np.exp(x) + x**2 - 10*x + 2

""" Let's calculate the derivative of f. Denote it with Df. """
x_minun_h = x - h
x_plus_h  = x + h
fx_minun_h = np.exp(x_minun_h) + x_minun_h**2 - 10*x_minun_h + 2
fx_plus_h  = np.exp(x_plus_h) + x_plus_h**2 - 10*x_plus_h + 2
Df = (fx_plus_h - fx_minun_h)/(2*h)

""" Form a spline using scipy library. 
    This is the derivative of f. """
Df_spline = interpolate.CubicSpline(x, Df)

""" Find the roots of Df(x) with Newton's method.

    Pick one random point between start and end point. 
    This is the x0 of the Newton's method,
    although quite confusingly we name it here x1,
    there is a technical reason for it. See how while loop works.
    
    A little hint: we are derivating here the derivative of f, so we handle
    the second order derivative of f. Let's name the second order derivative 
    as D2f. """

x1 = np.random.uniform(startPoint,endPoint,1)
while(test):
    iterations += 1
    x0 = x1
    
    """ Numerical derivation starts here. """
    """ For numerical derivation we need two points. """
    x_d = np.array([x0[0] + h, x0[0] - h])
    spline_numerator = Df_spline(x_d) 
    D2fx0 = (spline_numerator[0] - spline_numerator[1])/(2*h)
    """ Numerical derivation is done. """

    """ Something for the Newton's method. """
    Dfx0 = Df_spline(x0)
    """ The core of Newton's method. """
    x1 = x0 - Dfx0/D2fx0

    """ Test if we have result which is good enough, or if we are not going to
        find a good result. In these cases stop the algorithm. """
    if (Df_spline(x1)<targetAccuracy):
        test = False
        foundMinimumPoint = True
    elif(iterations > iterationRoundsMax):
        test = False
        foundMinimumPoint = False
        print('Calculation failed.')


""" Plot the result if we have a good result. """
if (foundMinimumPoint == True):
    """Minimum Point"""     
    fx1 = np.exp(x1) + x1**2 - 10*x1 + 2
    print('Minimum point: {:.7f}'.format(x1[0]))
    print('Minimum value: {:.7f}'.format(fx1[0]))
    
    """Plot the function and its derivative. """
    plt.plot(x,fx, c='r', label='f(x)')
    plt.plot(x, Df_spline(x), c='b', label='Df(x)')
    plt.scatter(x1[0],fx1[0], c='g', label='Minimum location')
    plt.legend(loc="upper left")
    plt.show()




















