import numpy as np

# 原始信号
x = np.array([1, 2, 3, 4])

# 计算DFT
X = np.fft.fft(x)

# 计算IDFT
x_recovered = np.fft.ifft(X)

print("原始信号：", x)
print("恢复后的信号：", x_recovered)


x = np.array([0, 1, 2, 3, 4, 5])
# x = np.roll(x, 2)
# print(x)

y = np.array([1,2,3,4,5, 6])

print(x * y)