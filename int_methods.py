import matplotlib.pyplot as plt


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


def simpson(xi, yi):
    n = len(xi)
    h = (xi[n - 1] - xi[0])/float(n)
    S = yi[0] + yi[n - 1]
    for i in range(0, n - 1, 2):
        S += 2 * yi[i]
    for i in range(0, n, 2):
        S += 4 * yi[i]
    S *= h/3.
    return S


def make_function(f, x, y, n):
    '''
    Collects n values of f equally spaced between x and y
    :param f: a function
    :param x: a number
    :param y: a number > x
    :param n: an integer
    :return: two tables: the table of abscissas and the table of the values of f corresponding to the abscissas
    '''
    xi = []
    yi = []
    h = (y - x)/float(n)
    for i in range(n + 1):
        xi.append(x + i * h)
        yi.append(f(xi[i]))
    return xi, yi


def plot_methods(f, x, y, n_min, n_max):
    '''
    Plots the result of each method on f between x and y, for each number of iterations between n_min and n_max
    :param f: a function
    :param x: a number
    :param y: a number > x
    :param n_min: an integer
    :param n_max: an integer > n_min
    '''
    val_rect_r = []
    val_rect_l = []
    val_midpoint = []
    val_trapezoidal = []
    val_simpson = []
    abscissas = range(n_min, n_max)
    for i in abscissas:
        xi, yi = make_function(f, x, y, i)
        val_rect_r.append(rect_r(xi, yi))
        val_rect_l.append(rect_l(xi, yi))
        val_midpoint.append(midpoint(xi, yi))
        val_trapezoidal.append(trapezoidal(xi, yi))
        val_simpson.append(simpson(xi, yi))

    r_r, = plt.plot(abscissas, val_rect_r, 'r', label='Rectangles right')
    r_l, = plt.plot(abscissas, val_rect_l, 'b', label='Rectangles left')
    mp, = plt.plot(abscissas, val_midpoint, 'g', label='Midpoint')
    tr, = plt.plot(abscissas, val_trapezoidal, 'y', label='Trapezoidal')
    s, = plt.plot(abscissas, val_simpson, 'k', label='Simpson')
    plt.legend([r_r, r_l, mp, tr, s], ['Rectangles right', 'Rectangles left', 'Midpoint', 'Trapezoidal', 'Simpson'], loc = 0)
    plt.xlabel('Number of iterations')
    plt.xscale('log')
    plt.show()


def f(x):
    return x**2

