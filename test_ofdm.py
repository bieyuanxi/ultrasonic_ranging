import unittest

import numpy as np

from ofdm import ofdm_modulate
from zc import generate_zc_sequence


class MyTestCase(unittest.TestCase):
    def test_modulate(self):
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        x = ofdm_modulate(zc, 960)

        self.assertEqual(True, np.all(x.imag < 1e-10))  # add assertion here


if __name__ == '__main__':
    unittest.main()
