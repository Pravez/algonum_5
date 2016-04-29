from airfoil_load import *
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

