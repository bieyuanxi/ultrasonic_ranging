import numpy as np
import matplotlib.pyplot as plt

# 采样频率
fs = 1000
# 采样点数
N = 1000
# 生成时间序列
t = np.arange(N)/fs
# 生成频率为50Hz的正弦波信号

f = 50 # 选择的频率应该 ≤ fs / 2，并且是 fs / N 的整数倍，前者是定理限制，后者是采样一个完整周期的整数倍
x = np.sin(2 * np.pi * f * t)
# x += np.sin(2 * np.pi * f1 * t)
# 进行FFT
X = np.fft.fft(x)
# 计算频率轴
k = np.arange(N)
frq = k * fs / N    # 频率域只能获取整数倍周期，值是fs / N的整数倍
# 只取前一半的频率分量（由于FFT的对称性）
frq1 = frq[range(int(N/2))]
X1 = X[range(int(N/2))]

# assert np.argmax(abs(X1)) == f
# 绘制频域图
plt.figure(1)
plt.plot(frq1, abs(X1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.figure(2)
plt.plot(t, x)
plt.xlabel('x')
plt.ylabel('y')



plt.show()