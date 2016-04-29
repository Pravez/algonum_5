from airfoil_load import *
import numpy as np
import matplotlib.pyplot as mp

#---------------#
#    LENGTH     #
#---------------#

''' Renvoie la longueur de la fonction de dérivée df entre x et y, avec n le nombre de subdivisions et I la fonction d'intégration utilisée '''


def length(I, n, df, x, y):
    length = lambda x: np.sqrt(1 + (df(x)*df(x)))
    return I(x, y, n, length) 


