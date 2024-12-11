import pyaudio
import wave

# 音频参数设置
FORMAT = pyaudio.paInt16  # 音频样本格式，这里使用16位整数格式
CHANNELS = 1  # 声道数，单声道设置为1，立体声设置为2
RATE = 48000  # 采样率，即每秒采集的样本数，常用的有44100Hz等
CHUNK = 1024  # 每次读取的音频数据块大小（以样本数为单位）
RECORD_SECONDS = 5  # 设定录制时长，这里设置为5秒，可按需调整
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"  # 保存录制音频的文件名

# 初始化PyAudio对象
audio = pyaudio.PyAudio()

# 打开音频流，配置音频输入参数
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("recording...")
frames = []
# 循环读取音频数据块并添加到列表中，实现音频录制
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("done")

# 停止音频流并关闭
stream.stop_stream()
stream.close()
# 终止PyAudio对象
audio.terminate()

# 将录制的音频数据保存为.wav文件
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_format_from_width(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()