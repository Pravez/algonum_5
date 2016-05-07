import numpy as np
import Spline as spline
import airfoil_load as airload
import matplotlib.pyplot as plt



def get_lambda_function(function, lambda_value, h):
    '''Gives lambda function according to lambda value, concerned function, and h (hmin or hmax)'''
    return (lambda x: (1-lambda_value)*function(x) + lambda_value*(3*h))

def create_pressures(h, func, precision, points_qty):

    pressures_array = []
    number = 0
    single_points_value = 1.0/points_qty

    for i in np.arange(0.0, 1.0, precision):
        pressures_array.append([])
        pressures_array[number].append([])
        pressures_array[number].append([])

        lambda_func = get_lambda_function(func, i, h)

        for k in range(0, points_qty):
            pressures_array[number][0].append(k*single_points_value)
            pressures_array[number][1].append(lambda_func(k*single_points_value))

        number+=1

    return pressures_array


def Create_pressure_map(file):
    (ex, ey, ix, iy) = airload.load_foil(file)

    hmin = np.min(iy)
    hmax = np.max(ey)

    func_intra = spline.get_func_splint(ix, iy)
    func_extra = spline.get_func_splint(ex, ey)


    pressure_extra = create_pressures(hmax, func_extra, 0.03, 170)
    pressure_intra = create_pressures(hmin, func_intra, 0.05, 170)

    plt.plot(ex, ey, color='red')
    plt.plot(ix, iy, color='red')

    for i in range (1, len(pressure_intra)):
        plt.plot(pressure_intra[i][0], pressure_intra[i][1], color='blue')

    for i in range(1, len(pressure_extra)):
        plt.plot(pressure_extra[i][0], pressure_extra[i][1], color='blue')

    plt.show()


Create_pressure_map("data/HOR20.DAT")