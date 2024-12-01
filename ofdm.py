import numpy as np

def ofdm_modulate(zc, N: int):
    """
    OFDM调制
    :param zc: Zadoff-Chu sequence
    :param N: len of a frame
    :return:
    """
    Nzc = len(zc)
    hzc = (Nzc - 1) // 2
    # Perform Nzc-point DFT on zc to get ZC
    ZC = np.fft.fft(zc, Nzc)

    # Frequency domain rearrangement
    ZC = np.roll(ZC, hzc)

    ### OFDM modulation ###
    X = np.zeros(N, dtype=complex)
    X[380 - hzc: 380 + hzc + 1] = ZC    # FIXME: 380 should be replaced with N * fc / fs!!!

    # 从index1开始，复制一半，翻转共轭
    X_half = X[1:(N + 1) // 2]
    X_half_conj = X_half[::-1].conj()
    X[N - N // 2 + 1:] = X_half_conj
    ### End of OFDM modulation ###

    assert np.array_equal(X[1:].conj(), X[:0:-1]) # 验证是否是共轭对称

    # Perform N-point IFFT on X to get x
    x = np.fft.ifft(X)
    return x


def ofdm_demodulate(y, N, fc, fs, N_prime, zc):
    """
    OFDM解调
    :param y: received signal sequence y[n]
    :param N: len of each frame
    :param fc: carrier frequency
    :param fs: sampling frequency
    :param N_prime:
    :param zc: zc sequence
    :return: Channel response sequence cir[n] of length N_prime for each frame
    """
    Nzc = len(zc)
    hzc = (Nzc - 1) // 2
    # Perform Nzc-point DFT on zc to get ZC
    ZC = np.fft.fft(zc, Nzc)

    # Frequency domain rearrangement
    ZC = np.roll(ZC, hzc)

    # Segment the received signal into frames with equal length of N
    num_segments = len(y) // N
    hzc = (len(zc) - 1) // 2
    if len(y) % N != 0:
        num_segments += 1

    nc = int(N * fc / fs)
    # TODO foreach frame y[n] of length N do
    for i in range(num_segments):
        # Perform N-point FFT on y[n] to get Y[n]
        Y = np.fft.fft(y[i * N: (i + 1) * N], N)

        # Conjugate multiplication
        CFR_hat = Y[nc - hzc:nc + hzc + 1] * ZC.conj()

        # Zero padding
        CFR = np.zeros(N_prime, dtype=complex)
        CFR[:hzc + 1] = CFR_hat[hzc:2 * hzc + 1]
        CFR[N_prime - 1:N_prime - 1 - hzc:-1] = CFR_hat[:hzc]

        # Perform N_prime-point IFFT on CFR[n] to get cir[n]
        cir = np.fft.ifft(CFR)
        return cir  # FIXME: foreach?


