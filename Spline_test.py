import unittest
import matplotlib.pyplot as plt
from airfoil_load import *
import Spline as spline


class Tests_Spline(unittest.TestCase):

    def test_with_goe144(self):
        file = ["data/goe144.dat", "data/HOR20.DAT"]

        for f in file:
            (ex, ey, ix, iy) = load_foil(f)

            extrados = spline.compute_smthing_dos(ex, ey, 10)
            intrados = spline.compute_smthing_dos(ix, iy, 10)
            plt.plot(extrados[0], extrados[1])
            plt.plot(intrados[0], intrados[1])
            plt.scatter(ex, ey, color='red')
            plt.scatter(ix, iy, color='red')
            plt.show()

if __name__ == '__main__':
    unittest.main()

