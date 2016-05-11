import numpy as np
import matplotlib.pyplot as plt

def spline(x, y, yp1, ypn, max):

    n = np.size(x) - 1
    u = np.zeros(n)
    y2 = np.zeros(n + 1)

    if(yp1 > max):
        y2[0] = u[0] = 0.0
    else:
        y2[0] = -0.5
        u[0] = (3.0 / (x[1] - x[0])) * ((y[1] - y[0]) / (x[1] - x[0]) - yp1)

    for i in range(1, n-1):
        sig = (x[i] - x[i-1]) / (x[i+1] - x[i-1])
        p = sig * y2[i-1] + 2.0
        y2[i] = (sig - 1.0) / p
        u[i] = (y[i+1] - y[i]) / (x[i+1] - x[i]) - (y[i] -y[i-1]) / (x[i] - x[i-1])
        u[i] = (6.0 * u[i] / (x[i+1] - x[i-1]) - sig * u[i-1]) / p

    if (ypn > max):
        qn = un = 0.0
    else:
        qn = 0.5
        un = (3.0 / (x[n] - x[n-1])) * (ypn - (y[n] - y[n-1]) / (x[n] - x[n-1]))

    y2[n] = (un - qn * u[n-1]) / (qn * y2[n-1] + 1.0)

    for k in range(n-1, 1, -1):
        y2[k] = y2[k] * y2[k+1] + u[k]

    return y2


def splint(xa, ya, y2a, n, x):
    klo = 0
    khi = n-1
    while khi-klo > 1 :
        k=(khi+klo) >> 1
        if(xa[k] > x):
            khi = k
        else:
            klo = k

    h = xa[khi] - xa[klo]
    if(h == 0.0):
        raise Exception("Error", "The xa's must be distinct")
    a = ( xa[khi] - x ) / h
    b = ( x - xa[klo] ) / h
    y = a * ya[klo] + b * ya[khi] + ((a * a * a - a) * y2a[klo] + (b * b * b - b) * y2a[khi]) * (h * h) / 6.0
    return y

def get_func_splint(xa, ya, yp1 = 1e30, ypn = 1e30, max = 0.99e30):
    n = len(xa)
    y2a = spline(xa, ya, yp1, ypn, max)

    return (lambda x: splint(xa, ya, y2a, n, x))

def compute_smthing_dos(xa, ya, npoints, yp1 = 1e30, ypn = 1e30):
    n = len(xa)

    value = (xa[n-1] / n) / npoints
    total_points = npoints * n + 1
    func = get_func_splint(xa, ya, yp1, ypn)

    final_points_y = []
    final_points_x = []

    for i in range(0, total_points):
        final_points_x.append(value*i)
        final_points_y.append(func(value*i))

    return [final_points_x, final_points_y]
