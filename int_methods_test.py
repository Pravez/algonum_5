import unittest
import int_methods as imet


class Tests_int_methods(unittest.TestCase):
    
    def test_plot_methods(self):
        imet.plot_methods(imet.f, 0, 10, 1, 1000)

    # def test_methods_accuracy(self):
    #     xi, yi = imet.make_function(lambda x: x, 0, 10, 100)
        


if __name__ == '__main__':
    unittest.main()
