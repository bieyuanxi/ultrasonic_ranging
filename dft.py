import numpy as np


def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)

    return np.dot(e, x)

def idft(X):
    N = len(X)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(1j * 2 * np.pi * k * n / N)
    x = np.dot(M, X) / N
    return x

if __name__ == "__main__":
    # 示例用法
    x = np.array([1, 2, 3, 4, 5])
    X = dft(x)

    print(X)
    # print(X.conjugate())

    x_recovered = idft(X)
    print(x_recovered)





# # numpy api
# import numpy as np
#
# # 原始信号
# x = np.array([1, 2, 3, 4])
#
# # 计算DFT
# X = np.fft.fft(x)
#
# # 计算IDFT
# x_recovered = np.fft.ifft(X)
#
# print("原始信号：", x)
# print("恢复后的信号：", x_recovered)