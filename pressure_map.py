import numpy as np
import matplotlib.pyplot as plt

#lowest and highest points of the airfoil
hmin=-3
hmax=3

#speed of the airfoil (resp. of the air around it), choosen for the examples in meter per second
V=300

#Approximate denity of the air in kg per cube meters
ro=1.225

#Function which determines the shape of the airfoil
def f(x):
    return 3-x**3

############### AUXILIAIRE FUNCTIONS ###############

#Computes the new function for a given lambda (between 0 and 1)
def flambdaUpper(x,l):
    return (1-l)*f(x) + l*3*hmax


#Computes the new function for a given lambda (between -1 and 0)
#At least I think 
def flambdaLower(x,l):
    return (l-1)*f(x) + l*3*hmin


#Returns the length of a given function, between two abscissa
#Precision is 10^-6 by default, can be modified
def length(l,x1,x2,eps=10**(-6)):
    length=0


    while(x1<x2):
        length+= np.sqrt((eps)**2 + (f(x1+eps,l)-f(x1,l))**2)
        x1+=eps
    return length

#Returns the speed of a fluid following the curve lambda = l, above the airfoil
def speedUpper(x1, x2, l, V):
    length=length(l,x1,x2)
    return length/(V/(x2-x1))

#Returns the pressure given a lambda
def dyn_pressure(x1, x2, l, V):
    return 0.5*1.225*(speedUpper(x1,x2,l,V))**2


#def horizontale_intersection_f(x1, x2, y1, y2)



#def print_airfoil(x1, x2, y1, y2, eps=0.1)
    
    


################# MAP PRESSURE ###################

# Prints a map of the pressure above an airfoil

# y1 = 3*hmin
# y2 = 3*hmax
#l = lambda , defines the precision 

def pressure_map(x1, x2, y1, y2, l, V=300):
    plt.title ("Pressure map")
    X=np.linspace(x1, x2, 300, endpoint=True)
    Y=f(X)
    plt.plot(X, Y, 'black')
    lmbda=l
    Pmax=dyn_pressure(x1,x2,l,V)
    while lmbda <= 1:
        Yl=flambdaUpper(X,lmbda)
        Pl=dyn_pressure(x1,x2,lmbda,V)
        cl=100*(Pl/Pmax)
        plt.plot(X, Yl, color=cl, linewidth=1, cmap=plt.get_cmap(hot)) 
    

    #print_airfoil(x1,x2,y1,y2)
    plt.show()
    




#http://www.labri.fr/perso/nrougier/teaching/matplotlib/#simple-plot
    
    
