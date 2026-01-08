import numpy as np
from pydub import AudioSegment

sound = AudioSegment.from_mp3("song.mp3")

samples = np.array(sound.get_array_of_samples())

print(samples)
sample_rate = sound.frame_rate
sample_width = sound.sample_width
channels = sound.channels
duration = len(sound) / 1000
print(sample_rate, sample_width, channels, duration)
samples = samples.reshape((-1, channels))
print(samples.min(), samples.max())
print(samples[10000:10020])


sample_rate_2 = 44100
duration_2 = 2.0
frequency = 349.228
frequency_2 = frequency * 2
frequency_3 = frequency * 3
frequency_4 = frequency * 4

# Define ADSR times in seconds
attack = 0.01
decay = 0.3
sustain_level = 0.0
release = 0.5

t = np.linspace(0, duration_2, int(sample_rate_2 * duration_2), endpoint=False)

wave = np.sin(2 * np.pi * frequency * t)
wave += np.sin(2 * np.pi * frequency_2 * t) / 2
wave += np.sin(2 * np.pi * frequency_3 * t) / 3
wave += np.sin(2 * np.pi * frequency_4 * t) / 4

wave /= np.max(np.abs(wave))

print(wave[10000:10020])
wave = wave * 0.25
print(wave[10000:10020])

# print(wave[:200])
# peaks = np.where(wave > 0.999)[0]
# print(peaks[:10])
# print(np.diff(peaks[:10]))

# wave = np.zeros_like(t)
# harmonics = [1, 2, 3, 4, 5]
# amplitudes = [1.0, 0.6, 0.3, 0.2, 0.1]
#
# for h, a in zip(harmonics, amplitudes):
#     wave += a * np.sin(2 * np.pi * fundamental * h * t)

wave_int16 = np.int16(wave * 32767)

audio = AudioSegment(
    wave_int16.tobytes(),
    frame_rate=sample_rate_2,
    sample_width=2,
    channels=1
)

audio.export("my_note.mp3", format="mp3")

# sound._data is a bytestring
# raw_data = sound.raw_data
# # print(raw_data)
#
#
# samples = np.array(sound.get_array_of_samples())
# if sound.channels == 2:
#     samples = samples.reshape((-1, 2))  # stereo: (samples, 2)


# from pydub import AudioSegment
# from pydub.utils import which
#
# print(which("ffmpeg"))  # ekstra tjek
#
# sound = AudioSegment.from_mp3("song.mp3")
# print(sound.frame_rate, sound.channels, sound.sample_width)