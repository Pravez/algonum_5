from airfoil_load import *
import matplotlib.pyplot as plt

(ex,ey,ix,iy) = load_foil('HOR20.DAT')

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
    klo = 1
    khi = n
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

#plt.plot(ix, iy)
#for i in range(ix.size):
#    plt.scatter(ix[i], iy[i])
#plt.show()

values = []
current = 0
i=0
while(current < ix[ix.size-1] and i < ix.size):
    current = 1e-3*i
    values.append(current)
    i+=1

print(values)
print(ix)

xa = []
ya = []
for i in range (ix.size):
    if(iy[i]> 1e-30):
        ya.append(iy[i])
        xa.append(ix[i])


yp1 = (ya[1] - ya[0])/(xa[1] - xa[0])
ypn = (ya[len(ya)-1] - ya[len(ya)-2]) / (xa[len(xa)-1] - xa[len(xa)-2])
y2a = spline(xa, ya, yp1, ypn, 1e-30)


d1 = []
for i in range(len(values)):
    d1.append(splint(xa, ya, y2a, len(xa)-1, values[i]))

plt.plot(values, d1)
plt.plot(xa, ya, color='red')
plt.show()

#il faut calculer les derivees premieres aux deux premiers points et aux deux derniers
