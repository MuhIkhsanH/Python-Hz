import pyaudio
import numpy as np

# Set parameters
chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100

p = pyaudio.PyAudio()

stream = p.open(format=format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)

print("Listening...")

while True:
    data = stream.read(chunk)
    data_np = np.frombuffer(data, dtype=np.int16)
    
    # Check if sound is above threshold
    if np.max(np.abs(data_np)) > 5:
        # Calculate FFT (Fast Fourier Transform)
        fft = np.fft.fft(data_np)
        frequencies = np.fft.fftfreq(len(fft), 1 / rate)
        
        # Find peak frequency
        peak_frequency = frequencies[np.argmax(np.abs(fft))]
        if abs(peak_frequency) > 200:
            print("Peak Frequency:", abs(peak_frequency), "Hz")
        else:
            pass
    

stream.stop_stream()
stream.close()
p.terminate()
