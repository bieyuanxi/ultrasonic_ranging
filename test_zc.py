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


    def test_zc_zc_conj(self):
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        multi = zc * zc.conjugate()
        print(multi.real)
        self.assertEqual(True, np.all(abs(multi) - 1 < 1e-10))  # add assertion here
        self.assertEqual(True, np.all(multi.real - 1 < 1e-10))  # add assertion here
        self.assertEqual(True, np.all(multi.imag < 1e-10))


    def test_zc_dot_zc_conj(self):
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        self.assertEqual(Nzc, np.dot(zc.conjugate(), zc))  # add assertion here


    def test_zc_ifft_dot_zc_conj_ifft(self):
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        ZC = np.fft.ifft(zc)

        ZC_shift = np.roll(ZC, 1)
        self.assertLess(abs(np.dot(ZC.conjugate(), ZC_shift)), 1e-10)

        ZC_shift = np.roll(ZC, 20)
        self.assertLess(abs(np.dot(ZC.conjugate(), ZC_shift)), 1e-10)

        ZC_shift = np.roll(ZC, 40)
        self.assertLess(1 - abs(np.dot(np.roll(ZC.conjugate(), 40), ZC_shift)), 1e-10)


    def test_zc_conj_dot_zc_fft(self):
        Nzc = 81
        zc = generate_zc_sequence(1, Nzc)
        ZC = np.fft.ifft(zc)

        ZC_shift = np.roll(ZC, 20)
        ZC1 = np.fft.fft(ZC_shift)
        self.assertLess(abs(np.dot(ZC.conjugate(), ZC_shift)), 1e-10)

        ZC_shift = np.roll(ZC, 40)
        ZC1 = np.fft.fft(ZC_shift)
        self.assertLess(1 - abs(np.dot(np.roll(ZC.conjugate(), 40), ZC_shift)), 1e-10)


    def test_zc_r(self):
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()
