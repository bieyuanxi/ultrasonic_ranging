import numpy as np

# 生成Zadoff-Chu序列
def generate_zc_sequence(r: int, Nzc: int):
    """
    生成ZC序列

    :param r: 根序列索引
    :param Nzc: ZC序列的长度
    :return: 生成的ZC序列
    """
    n = np.arange(Nzc)
    zc_sequence = np.exp(-1j * np.pi * r * n * (n + 1) / Nzc)

    return zc_sequence

if __name__ == "__main__":
    # 示例用法
    u = 1  # 根序列索引，可以根据需要修改
    Nzc = 9  # ZC序列的长度，可以根据需要修改

    zc_seq = generate_zc_sequence(u, Nzc)
    print("生成的ZC序列:", zc_seq)

    # X = np.zeros(Nzc, dtype=complex)
    # for k in range(0, Nzc):
    #     Xk = 0
    #     for n in range(0, Nzc):
    #         Xk += zc_seq[n] * np.exp(-1j * np.pi * 2 * n * k / Nzc)
    #     X[k] = Xk
    # print("生成的X序列:", X)

    X = np.zeros(Nzc, dtype=complex)
    k = np.arange(Nzc)
    for n in range(0, Nzc):
        X += zc_seq[n] * np.exp(-1j * np.pi * 2 * n * k / Nzc)

    print("生成的X序列:", X)
    Xconj = X.conjugate()

    print("生成的Xconj序列:", Xconj)

    for i in range(0, len(X)):
        Xroll = np.roll(X, i)
        dot = np.dot(Xroll, Xconj)
        print(abs(dot), dot)

    print("--------")

    ZCconj = zc_seq.conjugate()
    zc_seq = np.roll(zc_seq, -5)
    for i in range(0, len(zc_seq)):
        ZCroll = np.roll(zc_seq, i)
        dot = np.dot(ZCroll, ZCconj)
        print(abs(dot), dot)
