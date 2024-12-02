import numpy as np
from matplotlib import pyplot as plt

from zc import generate_zc_sequence

def abs_of_zc_is_1(Nzc):
    zc = generate_zc_sequence(1, Nzc)
    zc_abs = np.abs(zc)
    print(zc_abs)
    plt.plot(np.arange(len(zc_abs)), zc_abs)
    plt.xlabel('offset')
    plt.ylabel('cir')
    plt.title('')
    plt.show()


if __name__ == "__main__":
    abs_of_zc_is_1(Nzc=81)
