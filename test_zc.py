import unittest
import numpy as np

from zc import generate_zc_sequence


class MyTestCase(unittest.TestCase):
    """
    np.dot of zc conjugate sequence and zc sequence should be close to 0 for any shift which is not zero
    """
    def test_zc_shift_half(self):
        zc = generate_zc_sequence(1, 81)
        shift = len(zc) // 2
        zc_conj = zc.conjugate()
        zc_shift = np.roll(zc, shift)

        self.assertLess(abs(np.dot(zc_conj, zc_shift)), 1e-10)


    def test_zc_dot_zc_conj(self):
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        self.assertEqual(Nzc, np.dot(zc.conjugate(), zc))  # add assertion here



    def test_zc_r(self):
        pass    # TODO


if __name__ == '__main__':
    unittest.main()
