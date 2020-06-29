import transcription_tools.extract_audio as extract_audio
import transcription_tools.denoise as denoise
import transcription_tools.speech_to_text as speech_to_text
import transcription_tools.audio_conversion_pipe as audio_conversion_pipe

class Audio_Converter:
    def __init__(self, vfp = None, afp = None, tfp = None, dargs = None, v = False):
        self.video_file_path = vfp
        self.audio_file_path = afp
        self.text_file_path = tfp
        self.dargs = dargs
        self.ex_audio = extract_audio.Extract_Audio(vfp)
        self.denoise = denoise.Denoise()
        self.sp2txt = speech_to_text.Speech_To_Text(tfp)
        self.output = None
        self.v = v
        self.pipe = None
    def run(self):
        if self.v: print('initializing pipe...')
        pipe = audio_conversion_pipe.Audio_Conversion_Pipe([
            self.ex_audio, self.ex_audio, self.sp2txt
        ], v = self.v)
        
        if self.v: print('running pipe')
        self.output = pipe.run(self.audio_file_path)
        self.pipe = pipe.pipe
        
        return self.output