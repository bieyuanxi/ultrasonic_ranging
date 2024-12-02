import unittest

import numpy as np
import matplotlib.pyplot as plt

from ofdm import ofdm_modulate, ofdm_demodulate
from zc import generate_zc_sequence

def plot_ndarray(arr):
    plt.plot(np.arange(len(arr)), arr)
    plt.xlabel('offset')
    plt.ylabel('cir')
    plt.title('')
    plt.show()

class MyTestCase(unittest.TestCase):
    def test_modulate(self):
        """
        OFMD编码完成后应该为实数，即虚部为0
        """
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        x = ofdm_modulate(zc, 960)

        self.assertEqual(True, np.all(x.imag < 1e-10))  # imagine should be 0

    def test_demodulate(self):
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        x = ofdm_modulate(zc, 960)
        y = np.zeros(len(x) * 2, dtype=complex)
        y[:len(x)] = x
        y[len(x):] = x
        # y = y * 100
        y = np.roll(y, 400)
        cir = ofdm_demodulate(y, 960, 19, 48, 960 * 4, zc)
        print(cir)
        magnitude = np.abs(cir)
        print(np.argmax(magnitude))
        plot_ndarray(magnitude)


if __name__ == '__main__':
    unittest.main()
