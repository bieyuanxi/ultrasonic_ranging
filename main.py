import numpy as np

from ofdm import ofdm_modulate
from zc import generate_zc_sequence

# # 生成Zadoff-Chu序列
# def generate_zc_sequence(Nzc):
#     n = np.arange(Nzc)
#     zc = np.exp(-1j * np.pi * n * (n + 1) / Nzc)
#     return zc

# # OFDM调制
# def ofdm_modulate(zc, N: int):
#     hzc = (Nzc - 1) // 2
#     ZC = np.fft.fft(zc, Nzc)
#     ZC = np.roll(ZC, hzc)
#     # print(np.dot(ZC, ZC.conjugate()))
#     X = np.zeros(N, dtype=complex)
#     X[380 - hzc: 380 + hzc + 1] = ZC
#
#     # 从index1开始，复制一半，翻转共轭
#     X_half = X[1:(N + 1) // 2]
#     X_half_conj = X_half[::-1].conj()
#     X[N - N // 2 + 1:] = X_half_conj
#
#     assert np.array_equal(X[:].conj(), X[::-1]) # 验证是否是共轭对称
#     x = np.fft.ifft(X)
#     # print(x)
#     return x

# # OFDM解调
# def ofdm_demodulate(y, Nzc, N, fc, fs):
#     Y = np.fft.fft(y, N)
#     nc = int(N * fc / fs)
#     CFR = Y[380 + nc - hzc:380 + nc + hzc + 1] * zc.conj()
#     CFR = np.roll(CFR, hzc)
#     CFR = np.pad(CFR, (0, N - Nzc), 'constant')
#     cir = np.fft.ifft(CFR)
#     return cir

# OFDM解调
def ofdm_demodulate(y, Nzc, N, fc, fs):
    Y = np.fft.fft(y, N)
    nc = int(N * fc / fs)
    CFR = np.zeros(N_prime, dtype=complex)
    CFR1 = Y[380 + nc - hzc:380 + nc + hzc + 1] * zc.conj()
    CFR[:hzc + 1] = CFR1[hzc:2 * hzc + 1]

    CFR[N_prime - 2 * hzc - 1:N_prime - hzc - 1] = CFR1[hzc - 1::-1]
    # print(CFR[N_prime - 2 * hzc - 1:N_prime - hzc - 1])
    # print(CFR1[:hzc])
    # print(CFR1[hzc - 1::-1])

    cir = np.fft.ifft(CFR)
    return cir

# 计算距离
def calculate_distance(cir_aa, cir_ab, cir_ba, cir_bb, fs, N, N_prime, fc, c):
    m_aa = np.argmax(np.abs(cir_aa))
    m_ab = np.argmax(np.abs(cir_ab))
    m_ba = np.argmax(np.abs(cir_ba))
    m_bb = np.argmax(np.abs(cir_bb))

    phi_aa = np.angle(cir_aa[m_aa])
    phi_ab = np.angle(cir_ab[m_ab])
    phi_ba = np.angle(cir_ba[m_ba])
    phi_bb = np.angle(cir_bb[m_bb])

    m_sum = m_aa + m_bb - m_ab - m_ba
    phi_sum = phi_aa + phi_bb - phi_ab - phi_ba

    distance = (c * N_prime / (4 * fs * N_prime)) * m_sum + (c / (2 * np.pi * fc)) * phi_sum
    return distance

# 主函数
if __name__ == "__main__":
    # 系统参数
    fs = 48000
    N = 960
    Nzc = 81
    fc = 19000
    c = 343
    N_prime = 4 * N  # 设置N_prime的值

    # 生成ZC序列
    zc = generate_zc_sequence(1, Nzc)

    # 模拟设备A发送信号
    x = ofdm_modulate(zc, N)

    # 模拟设备B接收信号（添加一些延迟和噪声）
    delay = 100  # 示例延迟
    y = np.roll(x, delay) + 0.1 * np.random.randn(N)

    # OFDM解调
    hzc = (Nzc - 1) // 2
    cir_aa = ofdm_demodulate(x, Nzc, N, fc, fs)
    cir_ab = ofdm_demodulate(y, Nzc, N, fc, fs)

    # 模拟设备B发送信号
    x_b = ofdm_modulate(zc, N)

    # 模拟设备A接收信号（添加一些延迟和噪声）
    y_b = np.roll(x_b, delay) + 0.1 * np.random.randn(N)

    # OFDM解调
    cir_ba = ofdm_demodulate(y_b, Nzc, N, fc, fs)
    cir_bb = ofdm_demodulate(x_b, Nzc, N, fc, fs)

    # 计算距离
    distance = calculate_distance(cir_aa, cir_ab, cir_ba, cir_bb, fs, N, N_prime, fc, c)
    print("Calculated distance:", distance)