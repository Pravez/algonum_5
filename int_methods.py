def rect_r(f, a, b, n):
    h = (b - a)/float(n)
    S = 0
    for k in range(1, n+1):
        S += f(a + k*h)
    return h*S


def rect_l(f, a, b, n):
    h = (b - a)/float(n)
    S = 0
    for k in range(0, n):
        S += f(a + k*h)
    return h*S


def midpoint(f, a, b, n):
    h = (b - a)/float(n)
    S = 0
    for k in range(0, n+1):
        S += f(a + k*h + h/2.0)
    return h*S


def trapezoidal(f, a, b, n):
    h = (b - a)/float(n)
    S = 0
    m = (f(a) + f(b))/2.0
    for k in range(1, n):
        S += f(a + k*h)
    return h*(m + S)


def simpson(f, a, b, n):
    h = (b - a)/float(n)
    S = 0
    a0 = a
    for k in range(n):
        S += (h/6.)*(f(a0) + 4*f((2*a0+h)/2.) + f(a0 + h))
        a0 += h
    return S


# def f(x):
#     return x

# print(rect_r(f, 0, 1, 10))
# print(rect_l(f, 0, 1, 10))
# print(midpoint(f, 0, 1, 10))
# print(trapezoidal(f, 0, 1, 10))
# print(simpson(f, 0, 1, 10))

### La valeur exacte est 0.5 ###
