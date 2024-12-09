"""
一个有关傅立叶变换时间局限性的例子，表明不同的波形可能会有完全相同的频谱图
"""
import numpy as np
import matplotlib.pyplot as plt

def fft_case(x_seq, t_seq, figure_name):
    # 进行FFT
    X = np.fft.fft(x_seq)
    # 计算频率轴
    k = np.arange(N)
    frq = k * fs / N  # 频率域只能获取整数倍周期，值是fs / N的整数倍

    frq1 = frq[range(int(N // 2))]
    X1 = X[range(int(N // 2))]

    # 绘制频域图
    plt.figure(figure_name)

    plt.subplot(2, 1, 1)
    plt.plot(t_seq, x_seq)

    plt.subplot(2, 1, 2)
    plt.plot(frq1, abs(X1))


if __name__ == "__main__":
    # 采样频率
    fs = 1000
    # 采样点数
    N = 1000
    # 选择的频率应该 ≤ fs / 2，并且是 fs / N 的整数倍，前者是定理限制，后者是采样一个完整周期的整数倍
    f = 100
    f1 = 250
    # 生成时间序列
    t = np.arange(N) / fs

    # 波形a
    x = np.sin(2 * np.pi * f * t)
    x += np.sin(2 * np.pi * f1 * t)
    fft_case(x, t, 1)

    # 波形b
    x1 = np.sin(2 * np.pi * f * t[:len(t) // 2])
    x2 = np.sin(2 * np.pi * f1 * t[len(t) // 2:] * -1)
    x = np.concatenate((x1, x2), axis=0)
    fft_case(x, t, 2)

    # 波形c
    x1 = np.sin(2 * np.pi * f1 * t[:len(t) // 2])
    x2 = np.sin(2 * np.pi * f * t[len(t) // 2:] * -1)
    x = np.concatenate((x1, x2), axis=0)
    fft_case(x, t, 3)

    plt.show()