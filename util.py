import numpy as np
from matplotlib import pyplot as plt


def plot_ndarray(arr):
    plt.plot(np.arange(len(arr)), arr)
    plt.xlabel('offset')
    plt.ylabel('cir')
    plt.title('')
    plt.show()