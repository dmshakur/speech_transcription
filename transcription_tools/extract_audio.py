from pydub import AudioSegment

class Extract_Audio:
    def __init__(self, file_path, dargs = None):
        self.audio = AudioSegment.from_file(file_path, 'mp4')
    def run(self, audio_file_path):
        self.audio.export(audio_file_path, format="wav")
        return audio_file_path

# """
# n_grad_freq(int):
#     how many frequency channels to smooth over with the mask.
# n_grad_time(int):
#     how many time channels to smooth over with the mask.
# n_fft(int):
#     number audio of frames between STFT columns.
# win_length(int):
#     Each frame of audio is windowed by `window()`. 
#     The window will be of length `win_length` and 
#     then padded with zeros to match `n_fft`..
# hop_length(int):
#     number audio of frames between STFT columns.
# n_std_thresh(int):
#     how many standard deviations louder than the 
#     mean dB of the noise(at each frequency level) 
#     to be considered signal
# prop_decrease(float):
#     To what extent should you decrease noise(1=all, 0=none)
# pad_clipping(bool): 
#     Pad the signals with zeros to ensure that the 
#     reconstructed data is equal length to the data
# use_tensorflow(bool): 
#     Use tensorflow as a backend for convolution 
#     and fft to speed up computation
# verbose(bool): 
#     Whether to plot the steps of the algorithm
# """
