"""
pyaudio需要有库portaudio
Mac：
brew install portaudio

Linux：

Windows：
"""

import pyaudio
import numpy as np
import time

from ofdm import ofdm_modulate
from zc import generate_zc_sequence

# 采样率
sample_rate = 48000
# 每个声音持续时间（单位：秒）
duration = 1
volume = 1

Nzc = 81
N = 960

# 生成ZC序列
zc = generate_zc_sequence(1, Nzc)
# 模拟设备A发送信号
x = ofdm_modulate(zc, N)

# 定义生成指定频率音频波形数据的函数（同样生成正弦波）
def generate_tone(x):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    audio_data = x * (2**15 - 1) / np.max(np.abs(x))
    audio_data = (volume * audio_data).astype(np.int16)
    return audio_data

# 初始化PyAudio对象
p = pyaudio.PyAudio()

# 尝试发出不同频率的声音，这里以400Hz、600Hz、900Hz为例
frequencies = [19000, 21000]
for frequency in frequencies:
    audio_data = generate_tone(frequency)
    stream = p.open(format=p.get_format_from_width(2),
                    channels=1,
                    rate=sample_rate,
                    output=True)
    stream.write(audio_data.tobytes())
    time.sleep(0.5)
    stream.close()

p.terminate()