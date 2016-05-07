def rect_r(xi, yi):
    S = 0
    n = len(xi)
    for i in range(1, n):
        S += yi[i]
    h = (xi[n - 1] - xi[0])/float(n)
    return h*S


def rect_l(xi, yi):
    S = 0
    n = len(xi)
    for i in range(0, n - 1):
        S += yi[i]
    h = (xi[n - 1] - xi[0])/float(n)
    return h*S


def midpoint(xi, yi):
    n = len(xi)
    h = (xi[n - 1] - xi[0])/n
    S = 0
    for i in range(0, n - 1):
        S += (yi[i] + yi[i + 1])/2.0
    return h*S


def trapezoidal(xi, yi):
    n = len(xi)
    h = (xi[n - 1] - xi[0])/float(n)
    S = 0
    m = (xi[0] + xi[n - 1])/2.0
    for i in range(1, n):
        S += yi[i]
    return h*(m + S)


def find_abscissa(xi, val):
    for i in range(len(xi)):
        if val < xi[i]:
            return i - 1
    return len(xi)


def simpson(xi, yi):
    n = len(xi)
    h = (xi[n - 1] - xi[0])/float(n)
    S = 0
    for i in range(n - 1):
        x2 = (2 * xi[i] + h)/2.
        ind = find_abscissa(xi, x2)
        S += (h/6.) * (yi[i] + 4 * yi[ind] + yi[i + 1])
    return S


'''
xi = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
yi = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
print(rect_r(xi, yi))
print(rect_l(xi, yi))
print(midpoint(xi, yi))
print(trapezoidal(xi, yi))
print(simpson(xi, yi))

### La valeur exacte est 0.5 ###
'''