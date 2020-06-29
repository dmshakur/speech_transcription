import noisereduce as nr
from scipy.io.wavfile import write
from scipy.io import wavfile

class Denoise:
    def __init__(self):
        self.rate = None
        self.data = None
        self.reduced_noise = None
    def run(self, audio_file_path, dargs = None):
        reduced_path = 'denoised_' + audio_file_path
        print(audio_file_path)
        self.rate, self.data = wavfile.read(audio_file_path)
        if dargs is not None:
            self.reduced_noise = nr.reduce_noise(arg for arg in dargs)
        else:
            self.reduced_noise = nr.reduce_noise(audio_file_path)
        write(reduced_path, 44100, self.reduced_noise)
        return reduced_path
