
"""
Created on Wed Mar 17 17:29:48 2021

@author: siipola
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

""" Parameters explained.
 
    N:                  Number of points on the interval.
    initialStartPoint:  Leftmost point of the first interval.
    initialEndPoint:    Rightmost point of the first interval.    
    limitOfIterations:  Defines the number of iterations. 
    
    Algorithm explained.
    
    1: Calculate a set of points (x) between some interval on real line.
    2: Evalute the function f at these point.
    3: Find out which of the points (x) gives the minimum value of f.
    4: Find out if minimum point belongs to left or right half of the interval.
    5: Define a new interval. This new interval is either the left or right 
        half of the old interval.
    6: Repeat this algorithm for the number of 'limitOfIterations'.
    7: Print the result and plot of graph.
    
    
    Some inspiration for this algorithm may have come from Cantor set:
        https://en.wikipedia.org/wiki/Cantor_set
    """

""" Initialize the parameters of the model. """
N = 5000
initialStartPoint = -1
initialEndPoint = 5
limitOfIterations = 50

""" Technical update. """
startPoint = initialStartPoint
endPoint = initialEndPoint

""" Calculate the mid point of the interval. """
midPoint = (startPoint + endPoint)/2.0
for testRound in range(limitOfIterations):
    """ New set of points. """
    x = np.linspace(startPoint,endPoint, N)
    """ Calculate the function at these points. """
    fx = np.exp(x) + x**2 - 10*x + 2
    
    """ Calculate the minimum point (x). """
    x_min = x[np.argmin(fx)]
    """ Calculate the function at minimum point. 
        This is not really necessary anymore, it is just for fun. """
    fx_min = np.exp(x_min) + x_min**2 - 10*x_min + 2
    
    """ Update the interval. """
    if (x_min < midPoint):
        """ If the minimum point lies on the left side of the center of the 
            interval, then the next interval is formed in such a way that
            leftmost point is the same as before and center point is going to
            be the rightmost point."""
        endPoint = midPoint
    elif (x_min >= midPoint):
        """ If minimum point (x) lies on the rightside of the interval, then
            the center point of the old interval becomes the leftmost point
            in the new interval. """
        startPoint = midPoint
    else:
        print('Something went wrong!')
        sys.exit()
    """ Calculate the center point of the new interval. """
    midPoint = (startPoint + endPoint)/2.0
""" Algortihm ends here. """


""" Plot the result. """
x = np.linspace(initialStartPoint, initialEndPoint, N)
fx = np.exp(x) + x**2 - 10*x + 2
print('Minimum point: {:.7f}'.format(x_min))
print('Minimum value: {:.7f}'.format(fx_min))

"""Plot the function. """
plt.plot(x,fx, c='r', label='f(x)')
plt.scatter(x_min,fx_min, c='g', label='Minimum location')
plt.legend(loc="upper left")
plt.show()



















