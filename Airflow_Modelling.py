import numpy as np
import Spline as spline
import length as length
import airfoil_load as airload
import matplotlib.pyplot as plt


def get_pixels(valuex, valuey):
    pixels = [[] for i in range(0, valuex)]
    for i in range(0, valuex):
        pixels[i] = [[] for k in range(0, valuey)]
        for j in range(0, valuey):
            pixels[i][j] = 0.0

    return pixels

def locate_pixel(x, y, pix, pressures, pitch):
    #first we define the x position corresponding in the pressure map
    x_var = 0.0
    x_pos = 0
    while x > x_var:
        x_var+= pitch
        x_pos+=1
    #then the number of curve
    i = 0
    if(y > 0):
        while y > pressures[i][1][x_pos] and y != 0.0:
            i+=1
    else:
        while y < pressures[i][1][x_pos] and y != 0.0:
            i+=1

    return i


def create_colors(pressures_extra, pressures_intra, pressures_length_extra, pressures_length_intra):

    pixels_extra = get_pixels(300,300)
    pixels_intra = get_pixels(300, 50)

    for i in range(0, len(pixels_extra)):
        for j in range(0, len(pixels_extra[i])):
            #0.36 corresponds to max value (extra)
            value = locate_pixel(i/304.0, j/(300/0.36), pixels_extra[i][j], pressures_extra, 0.002)
            if value == 0:
                pixels_extra[i][j] = 1.0
            else:
                pixels_extra[i][j] = pressures_length_extra[value]

    for i in range(0, len(pixels_intra)):
        for j in range(0, len(pixels_intra[i])):
            #0.23 corresponds to min value (intra)
            value = locate_pixel(i/303.0, -j/(50/0.23), pixels_intra[i][j], pressures_intra, 0.002)
            if value == 0:
                pixels_intra[i][j] = 1.0
            else:
                pixels_intra[i][j] = pressures_length_intra[value]

    #plt.imshow(pixels_intra, cmap="hot")
    #plt.show()

    pixels = get_pixels(350, 300)
    for i in range(0, 300):
        for j in range(0, 350):
            if(j<300):
                pixels[j][i] = pixels_extra[i][299-j]
            else:
                pixels[j][i] = pixels_intra[i][j-349]

    return pixels

def get_lambda_function(function, lambda_value, h):
    '''Gives lambda function according to lambda value, concerned function, and h (hmin or hmax)'''
    return (lambda x: (1-lambda_value)*function(x) + lambda_value*(3*h))

def create_pressures(h, func, precision, points_qty):
    '''Creates pressures for a given h and function'''
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

def compute_pressure_with_speed(pressures_array):

    pressure_speed = []
    for i in range(0, len(pressures_array)):
        pressure_speed.append(length.length2(pressures_array[i][0], pressures_array[i][1], length.simpson))

    return pressure_speed


def Create_pressure_map(file):
    (ex, ey, ix, iy) = airload.load_foil(file)

    hmin = np.min(iy)
    hmax = np.max(ey)

    func_intra = spline.get_func_splint(ix, iy)
    func_extra = spline.get_func_splint(ex, ey)


    #We define here pressures on the upper and lower part of the wing
    pressure_extra = create_pressures(hmax, func_extra, 0.01, 500)
    pressure_intra = create_pressures(hmin, func_intra, 0.03, 500)

    orig_extra = spline.compute_smthing_dos(ex, ey, 200)
    orig_intra = spline.compute_smthing_dos(ix, iy, 200)

    plt.plot(orig_extra[0], orig_extra[1], color='red')
    plt.plot(orig_intra[0], orig_intra[1], color='red')

    for i in range (1, len(pressure_intra)):
     plt.plot(pressure_intra[i][0], pressure_intra[i][1], color='blue')

    for i in range(1, len(pressure_extra)):
     plt.plot(pressure_extra[i][0], pressure_extra[i][1], color='blue')


    plt.title("Pressure map")
    plt.show()

    length_extra = (compute_pressure_with_speed(pressure_extra))
    length_intra = (compute_pressure_with_speed(pressure_intra))

    #now we create a pixel map for the colors
    result = create_colors(pressure_extra, pressure_intra, length_extra, length_intra)

    plt.imshow(result, cmap="hot")
    plt.show()





#Be careful when changing file, min and max values in calculations are made manually.
Create_pressure_map("data/HOR20.DAT")