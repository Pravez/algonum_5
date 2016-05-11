from airfoil_load import *
from int_methods import *
import numpy as np
import matplotlib.pyplot as mp

#---------------#
#    LENGTH     #
#---------------#

''' Renvoie la longueur de la fonction de derivee df entre x et y, avec n le nombre de subdivisions et I la fonction d'integration utilisee '''


def length(I, n, df, x, y):
    length = lambda x: np.sqrt(1 + (df(x)*df(x)))
    return I(x, y, n, length) 

def derivate(Pol):
    n = Pol.shape[0]
    m = Pol.shape[1]
    dPol = np.zeros([n,m])
    
    for i in np.arange(0,n):
        dPol[i][0] = 0
        dPol[i][1] = 3*Pol[i][0]
        dPol[i][2] = 2*Pol[i][1]
        dPol[i][3] = Pol[i][2]
        
    return dPol


def deriv(xi, yi):
    '''
    Takes a function f represented by an array of abscissas and an array of images and returns an array of the same length representing f'
    :param xi: an array of abscissas
    :param yi: an array of values of f corresponding to the abscissas xi
    :return: an array of values of f' corresponding to the abscissas xi
    '''
    n = len(xi)
    f_der = [yi[0]]
    for i in range(1, n - 1):
        pente = (yi[i + 1] - yi[i - 1])/(xi[i + 1] - xi[i - 1])
        f_der.append(pente)
    f_der.append(yi[n-1])
    return f_der


def length2(xi, yi, method):
    '''
    Returns the length of the graph of f between x and y based on the formula given in the subject, the integration method can be chosen
    :param xi: an array representing the abscissas
    :param yi: an array reprensenting the values of f at each point of xi
    :param method: a function
    :return: the length of f's graph
    '''
    df = deriv(xi, yi)
    integrand = []
    for i in range(len(xi)):
        integrand.append(1 + df[i]**2)
    return method(xi, integrand)


#xi = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#yi = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#print(deriv(xi, yi))
#print(length2(xi, yi, simpson))