import numpy as np
from pydub import AudioSegment

sound = AudioSegment.from_mp3("song.mp3")

# sound._data is a bytestring
raw_data = sound.raw_data
# print(raw_data)


samples = np.array(sound.get_array_of_samples())
if sound.channels == 2:
    samples = samples.reshape((-1, 2))  # stereo: (samples, 2)


# from pydub import AudioSegment
# from pydub.utils import which
#
# print(which("ffmpeg"))  # ekstra tjek
#
# sound = AudioSegment.from_mp3("song.mp3")
# print(sound.frame_rate, sound.channels, sound.sample_width)