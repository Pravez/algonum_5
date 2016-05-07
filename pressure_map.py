import numpy as np
import matplotlib.pyplot as plt

hmin=-3
hmax=3

ro=

def f(x):
    return x³


def flambdaUpper(x,l):
    return (1-l)*f(x) + l*3*hmax


def flambdaLower(x,l):
    return (1-l)*f(x) + l*3*hmin


#Returns the length of a given function, between two abscissa
#Precision is 10^-6 by default, can be modified
def length(f,l,x1,x2,eps=10**(-6)):
    length=0
    
    while(x1<x2):
        length+= np.sqrt((eps)**2 + (f(x1+eps,l)-f(x1,l))**2)
        x1+=eps
    return length

#Returns the speed of a fluid following the curve lambda = l, above the airfoil

def speedUpper(flambdaUpper,l,x1,x2,V):
    length=length(flambdaUpper,l,x1,x2)
    return length/(V/(x2-x1))

# y1 = 3*hmin
# y2 = 3*hmax
#l = lambda , defines the precision 

def pressure_map(x1, x2, y1, y2, l):
    plt.title ("Pressure map")
    X=np.linspace(x1, x2, (x2 - x1)/l, endpoint=True)
    Y=f(X)
    plt.plot(X, Y, 'black')
    for 
    Yl=flambdaUpper(X,l)
    



http://www.labri.fr/perso/nrougier/teaching/matplotlib/#simple-plot
    
    
