from google.cloud import speech
from google.cloud.speech import types
import speech_recognition as sr
import os
import pickle


class Speech_To_Text:
    def __init__(self, sp2txt_path=None):
        self.r = sr.Recognizer()
        self.text = None
        self.audio = None
        self.sp2txt_path = sp2txt_path
        self.lang = 'en-US'
        # self.client = speech.SpeechClient()

    def run(self, audio_file_path):
        # with io.open(audio_file_path, 'rb') as audio_file:
        #     content = audio_file.read()
        # self.audio = types.RecognitionAudio(content=content)
        # config = types.RecognitionConfig(
        #     sample_rate_hertz=44100,
        #     language_code = self.lang)
        # self.text = self.client.recognize(config, self.audio)
        # pickle_out = open("sp2txt.pickle","wb")
        # pickle.dump(self.text, pickle_out)
        # pickle_out.close()
        # return self.text
        with sr.AudioFile(audio_file_path) as source:
            self.audio = self.r.record(source)
        print(GOOGLE_CLOUD_SPEECH_CREDENTIALS)
        try:
            self.text = self.r.recognize_google_cloud(self.audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            print("Google Cloud Speech thinks you said " + self.text)

            text_file = open(self.sp2txt_path, 'w+')
            text_file.write(self.text)
            pickle_out = open(self.sp2txt_path[:-4] + '.pickle', 'wb')
            pickle.dump(self.text, pickle_out)

            pickle_out.close()
            text_file.close()

            return self.text
            
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Cloud Speech service; {0}".format(e))

        # self.text = self.r.recognize_sphinx(self.audio)
