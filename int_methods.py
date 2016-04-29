def rect_r(f, a, b, n):
    h = (b - a)/n
    S = 0
    for k in range(1, n+1):
        S += f(a + k*h)
    return h*S


def rect_l(f, a, b, n):
    h = (b - a)/n
    S = 0
    for k in range(0, n):
        S += f(a + k*h)
    return h*S


def midpoint(f, a, b, n):
    h = (b - a)/n
    S = 0
    for k in range(0, n+1):
        S += f(a + k*h + h/2)
    return h*S


def trapezoidal(f, a, b, n):
    h = (b - a)/n
    S = 0
    m = (f(a) + f(b))/2
    for k in range(1, n):
        S += f(a + k*h)
    return h*(m + S)


