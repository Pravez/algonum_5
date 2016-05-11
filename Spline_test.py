import unittest
import matplotlib.pyplot as plt
from airfoil_load import *
import Spline as spline


class Tests_Spline(unittest.TestCase):

    def test_with_goe144(self):
        file = ["data/goe144.dat"]

        for f in file:
            (ex, ey, ix, iy) = load_foil(f)

            extrados = spline.compute_smthing_dos(ex, ey, 100)
            intrados = spline.compute_smthing_dos(ix, iy, 100)
            plt.plot(extrados[0], extrados[1], color='green')
            plt.plot(intrados[0], intrados[1], color='green')
            plt.plot([0, 1], [0, 0], color='black')
            plt.scatter(ex, ey, color='red')
            plt.scatter(ix, iy, color='red')
            plt.xlim((0, 1))
            plt.ylim((-0.02, 0.09))
            plt.title("Interpolated curve and original points of goe144")
            plt.show()

if __name__ == '__main__':
    unittest.main()

