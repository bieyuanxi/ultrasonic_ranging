import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

if __name__ == "__main__":
   # 生成示例信号
   fs = 44100  # 采样率
   t = np.linspace(0, 1, fs, endpoint=False)
   signal = np.sin(2 * np.pi * 19000 * t)  # 440Hz的正弦波

   # 进行FFT
   fft_result = fft(signal)
   # fft_result = np.fft.fft(signal)
   freqs = np.fft.fftfreq(len(signal), 1/fs)

   # 绘制频谱图
   plt.plot(freqs[:len(freqs)//2], np.abs(fft_result[:len(fft_result)//2]))
   plt.xlabel('Frequency (Hz)')
   plt.ylabel('Amplitude')
   plt.title('Frequency Spectrum')
   plt.show()