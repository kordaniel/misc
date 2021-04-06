#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:45:45 2021

@author: siipola
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

"""ex1."""
print('Some plots for the ex1.')
x = np.linspace(-5,5,10000)
x.shape = (len(x),1)
"""ReLu"""
fx = np.maximum(0,x)
plt.title("ReLu")
plt.plot(x,fx)
#plt.savefig('ex_1_1_plot_ReLu.png')
plt.show()

"""Derivative of ReLu"""
Dfx = np.zeros_like(x)
Dfx[x[:,0]<0, 0] = 0
Dfx[x[:,0]>0, 0] = 1
""" How to handle the undefined point. """
Dfx[x[:,0]==0, 0] = 0
plt.title("Derivative of ReLu")
plt.plot(x,Dfx)
#plt.savefig('ex_1_1_plot_Derivative_of_ReLu.png')
plt.show()

"""tanh"""
fx = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
plt.title("tanh")
plt.plot(x,fx)
#plt.savefig('ex_1_1_plot_tanh.png')
plt.show()

"""Derivative of tanh"""
Dfx = 4/((np.exp(x)+np.exp(-x))**2)
plt.title("Derivative of tanh")
plt.plot(x,Dfx)
#plt.savefig('ex_1_1_plot_Derivative_of_tanh.png')
plt.show()

"""sigmoid"""
fx = 1/(1+np.exp(-x))
plt.title("sigmoid")
plt.plot(x,fx)
#plt.savefig('ex_1_1_plot_Sigmoid.png')
plt.show()

"""derivative of sigmoid"""
Dfx = np.exp(-x)/((1+np.exp(-x))**2)
plt.title("derivative of sigmoid")
plt.plot(x,Dfx)
#plt.savefig('ex_1_1_plot_Derivative_of_Sigmoid.png')
plt.show()

"""softplus"""
fx = np.log(1+np.exp(x))
plt.title("softplus")
plt.plot(x,fx)
#plt.savefig('ex_1_1_plot_Softplus.png')
plt.show()

Dfx = np.exp(x)/(1+np.exp(x))
plt.title("derivative of softplus")
plt.plot(x,Dfx)
#plt.savefig('ex_1_1_plot_Derivative_of_Softplus.png')
plt.show()

"""Bent identity"""
fx = 0.5*(np.sqrt(x**2+1)-1)+x
plt.title("Bent identity")
plt.plot(x,fx)
#plt.savefig('ex_1_1_plot_Bent_identity.png')
plt.show()

Dfx = x/(2.0*np.sqrt(x**2+1))+1
plt.title("Derivative of Bent identity")
plt.plot(x,Dfx)
#plt.savefig('ex_1_1_plot_Derivative_of_Bent_identity.png')
plt.show()



""" ex2. """
print('Some plots for the ex2.')
""" Define x: """
x = np.linspace(-5,5,1000)
x.shape = (len(x),1)

""" Define the function f(x): """
fx = np.zeros_like(x)
fx[x[:,0]>2, 0] = 1.0
interval_points = np.logical_and(x[:,0]<2,x[:,0]>0)
fx[interval_points, 0] = x[interval_points, 0]-(1/4)*(x[interval_points, 0]**2)
interval_points = np.logical_and(x[:,0]<0,x[:,0]>-2)
fx[interval_points, 0] = x[interval_points, 0]+(1/4)*(x[interval_points, 0]**2)
fx[x[:,0]<-2, 0] = -1.0

""" Plot the function. """
plt.title("Square Nonlinearity (SQNL)")
plt.plot(x,fx)
#plt.savefig('ex_1_2_plot_SQNL.png')
plt.show()

Dfx = np.zeros_like(x)
Dfx[x[:,0]>2, 0] = 0.0
interval_points = np.logical_and(x[:,0]<2,x[:,0]>0)
Dfx[interval_points, 0] = 1.0-(1/2)*x[interval_points, 0]
interval_points = np.logical_and(x[:,0]<0,x[:,0]>-2)
Dfx[interval_points, 0] = 1.0+(1/2)*x[interval_points, 0]
Dfx[x[:,0]<-2, 0] = 0.0

""" Plot the derivative of the function. """
plt.title("Derivative of Square Nonlinearity (SQNL)")
plt.plot(x,Dfx)
#plt.savefig('ex_1_2_plot_Derivative_of_SQNL.png')
plt.show()


""" ex3. 
    This plotting requires is a bit more work when compared to previous plots. 
    
    You can play around with the parameters of the plot. 

    """
print('Some plots for the ex3.')
a = -3 # Start point of the interval.
b = 3  # end point of the interval.
N = 100 # Number of point on the interval.
n_max = 6 # How many different H_n functions is drawn. Starting from 0.
h = 1e-6

for n in range(n_max):
#    x = np.random.uniform(low=a, high=b, size=N) # Set of point from the interval [a,b].
#    x = np.sort(x)
    x = np.linspace(a,b,N) 
    x_plus_h = x + h # Set of points for the derivation.
    x_minus_h = x - h # Set of points for the derivation.
    if (n == 0):
        Hnx = (-1)**n*np.exp(0.5*x**2)*np.exp(-0.5*x**2)
    elif (n == 1):
        exp_x_plus_h = np.exp(-0.5*x_plus_h**2)
        exp_x_minun_h = np.exp(-0.5*x_minus_h**2)
        Dexp_x = (exp_x_plus_h - exp_x_minun_h)/(2*h)
        Dexp_spline = interpolate.CubicSpline(x, Dexp_x)
        Hnx = (-1)**n*np.exp(0.5*x**2)*Dexp_spline(x)
    else:
        Dn_exp_plus_h = Dexp_spline(x_plus_h)
        Dn_exp_minus_h = Dexp_spline(x_minus_h)
        D_n_plus_1_exp_x = (Dn_exp_plus_h - Dn_exp_minus_h)/(2*h)
        Dexp_spline = interpolate.CubicSpline(x, D_n_plus_1_exp_x)
        Hnx = ((-1)**n)*np.exp(0.5*x**2)*Dexp_spline(x)
        
    """Plot the function H_n(x). """
    plt.plot(x[2:-2],Hnx[2:-2], label='H_{}(x)'.format(n))
    plt.legend(loc="upper left")
#plt.savefig('ex_1_3_plot_Hn.png')
plt.show()

