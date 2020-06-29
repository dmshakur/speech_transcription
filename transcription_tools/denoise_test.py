import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal
import matplotlib.pyplot as plt

# Replace this with the location of your downloaded file.
audio_file_path = None
(Frequency, array) = read(audio_file_path) # Reading the sound file. 

len(array) # length of our array

FourierTransformation = sp.fft(array) # Calculating the fourier transformation of the signal

scale = sp.linspace(0, Frequency, len(array))

# plt.stem(scale[0:5000], np.abs(FourierTransformation[0:5000]), 'r')  # The size of our diagram
# plt.title('Signal spectrum after FFT')
# plt.xlabel('Frequency(Hz)')
# plt.ylabel('Amplitude')

GuassianNoise = np.random.rand(len(FourierTransformation)) # Adding guassian Noise to the signal.
NewSound = GuassianNoise + array

write("New-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound) # Saving it to the file.

b,a = signal.butter(5, 1000/(Frequency/2), btype='highpass') # ButterWorth filter 4350

filteredSignal = signal.lfilter(b,a,NewSound)

# plt.plot(filteredSignal) # plotting the signal.
# plt.title('Highpass Filter')
# plt.xlabel('Frequency(Hz)')
# plt.ylabel('Amplitude')

c,d = signal.butter(5, 380/(Frequency/2), btype='lowpass') # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal

# plt.plot(newFilteredSignal) # plotting the signal.
# plt.title('Lowpass Filter')
# plt.xlabel('Frequency(Hz)')
# plt.ylabel('Amplitude')

write("New-Filtered-Eagle-Sound.wav", Frequency, newFilteredSignal) # Saving it to the file.