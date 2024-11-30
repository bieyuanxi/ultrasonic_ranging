import numpy as np

# OFDM调制
def ofdm_modulate(zc, N: int):
    Nzc = len(zc)
    hzc = (Nzc - 1) // 2
    ZC = np.fft.fft(zc, Nzc)
    ZC = np.roll(ZC, hzc)
    # print(np.dot(ZC, ZC.conjugate()))
    X = np.zeros(N, dtype=complex)
    X[380 - hzc: 380 + hzc + 1] = ZC    # FIXME: 380 should be replaced with N * fc / fs!!!

    # 从index1开始，复制一半，翻转共轭
    X_half = X[1:(N + 1) // 2]
    X_half_conj = X_half[::-1].conj()
    X[N - N // 2 + 1:] = X_half_conj

    assert np.array_equal(X[1:].conj(), X[:0:-1]) # 验证是否是共轭对称
    x = np.fft.ifft(X)
    return x