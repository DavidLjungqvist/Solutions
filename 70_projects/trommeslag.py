import librosa

# Replace "song.mp3" with your file path
audio_path = "song.mp3"

# Load the audio file
y, sr = librosa.load(audio_path, sr=None, mono=True)

# Check that it loaded correctly
print(f"Audio loaded: {len(y)} samples, sample rate: {sr} Hz")

