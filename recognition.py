import librosa

audio_path = r"C:\Users\nish\Desktop\Projects\Spyder Projects\SPeechRecognition\audio2.wav"

x , sr = librosa.load(audio_path)

import matplotlib.pyplot as plt
import librosa.display
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
