import numpy as np
import scipy.io.wavfile
import scipy.signal
import sounddevice as sd

def high_pass_filter(data, rate, cutoff=20000):
    """Apply a high-pass filter to isolate ultrasonic components."""
    sos = scipy.signal.butter(10, cutoff, 'hp', fs=rate, output='sos')
    filtered = scipy.signal.sosfilt(sos, data)
    return filtered

def analyze_and_play(file_name):
    #Read audio file
    rate, data = scipy.io.wavfile.read(file_name)
    data = data.astype(np.float32)

    # Apply Fast Fourier Transform to find peak frequency
    freqs = np.fft.fftfreq(len(data), 1/rate)
    fft_spectrum = np.fft.fft(data)
    ultrasonic_freqs = np.abs(freqs[np.abs(freqs) > 20000])
    ultrasonic_spectrum = fft_spectrum[np.abs(freqs) > 20000]
    peak_freq = ultrasonic_freqs[np.argmax(np.abs(ultrasonic_spectrum))]

    #check for significant ultrasonic component
    threshold = 1000  # Adjust as needed
    if np.max(np.abs(ultrasonic_spectrum)) > threshold and peak_freq > 20000:
        print(f"Ultrasonic signal detected in {file_name} at {peak_freq} Hz")

        #Apply high-pass filter to isolate ultrasonic component
        ultrasonic_data = high_pass_filter(data, rate)

        # Attempt a simple amplitude demodulation
        demodulated_signal = np.abs(ultrasonic_data)

        #Downsample to make it audible
        new_rate = 44100  # Standard audio rate
        audible_signal = scipy.signal.resample(demodulated_signal, int(len(demodulated_signal) * (new_rate / rate)))

        #Modified audio
        sd.play(audible_signal, new_rate)
        sd.wait()
    else:
        print(f"No significant ultrasonic signal in {file_name}")

files_to_check = ["Ex3_sound2.wav", "Ex3_sound3.wav", "Ex3_sound4.wav"]
for file in files_to_check:
    analyze_and_play(file)
