import numpy as np
from matplotlib import pyplot as plt

from ofdm import ofdm_modulate, ofdm_demodulate
from zc import generate_zc_sequence
from util import plot_ndarray

Nzc = 81
N = 960
zc = generate_zc_sequence(1, Nzc)
x = ofdm_modulate(zc, N)

assert np.all(x.imag < 1e-10)

# X = np.fft.fft(x, N)    # == half shifted ZC
# plt.plot(np.arange(len(X)), X)
# plt.xlabel('offset')
# plt.ylabel('cir')
# plt.title('')
#
y = np.roll(x, 100)    # delay 100
#
# Y = np.fft.fft(y)
# plt.plot(np.arange(len(Y)), Y)
# plt.xlabel('offset')
# plt.ylabel('cir')
# plt.title('')



cir = ofdm_demodulate(y, N, 19, 48, N * 4, zc)
magnitude = np.abs(cir)
print(len(magnitude))
plt.plot(np.arange(len(magnitude)), magnitude)
plt.xlabel('offset')
plt.ylabel('cir')
plt.title('')


plt.show()