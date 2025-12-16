import librosa
import soundfile as sf

# Replace "song.mp3" with your file path
audio_path = "song.mp3"

# Load the audio file
y, sr = librosa.load(audio_path, sr=None, mono=True)

# Check that it loaded correctly
print(f"Audio loaded: {len(y)} samples, sample rate: {sr} Hz")

y_harmonic, y_percussive = librosa.effects.hpss(y)

# Optional: check lengths and type
print(f"Harmonic part: {len(y_harmonic)} samples")
print(f"Percussive part (drums): {len(y_percussive)} samples")


# Save the separated signals
sf.write("harmonic.wav", y_harmonic, sr)
sf.write("percussive.wav", y_percussive, sr)

print("Saved harmonic.wav and percussive.wav")

onset_env = librosa.onset.onset_strength(y=y_percussive, sr=sr)
tempo, beat_frames = librosa.beat.beat_track(
    onset_envelope=onset_env,
    sr=sr
)

print(f"Tempo:{tempo}, Beat frames: {beat_frames}")