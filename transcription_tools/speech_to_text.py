import speech_recognition as sr
import json
import pickle

class Speech_To_Text:
    def __init__(self, sp2txt_path=None):
        self.r = sr.Recognizer()
        self.text = None
        self.audio = None
        self.sp2txt_path = sp2txt_path
        self.lang = 'en-US'

    def run(self, audio_file_path):
        with sr.AudioFile(audio_file_path) as source:
            self.audio = self.r.record(source)

        ibm_cred = open('./ibm_credentials.json', 'r')
        ibm_cred = ibm_cred.read()
        ibm_cred = json.loads(ibm_cred)
        
        IBM_USERNAME = ibm_cred['ibm_username']  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
        IBM_PASSWORD = ibm_cred['ibm_password']  # IBM Speech to Text passwords are mixed-case alphanumeric strings

        try:
            self.text = self.r.recognize_ibm(self.audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        
            text_file = open(self.sp2txt_path, 'w+')
            text_file.write(self.text)
            pickle_out = open(self.sp2txt_path[:-4] + '.pickle', 'wb')
            pickle.dump(self.text, pickle_out)

            pickle_out.close()
            text_file.close()

            return self.text
        except sr.UnknownValueError:
            print("IBM Speech to Text could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from IBM Speech to Text service; {0}".format(e))