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
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
            {
              "type": "service_account",
              "project_id": "glassy-strata-278319",
              "private_key_id": "18ab22184ead70c6601e4272daee1b1c710778b2",
              "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCZH8OFi4OClXOR\n+DRzFrKNHR6hqOQkl2LDg3WNtzVDwSJnEfoyqKttCW6H85tU7t+GrTBlPyHOZgmZ\nGbOhgLQg8/da+21iYmQhM6X9tY91/WiJIulnIDy9Qx/vM5qLIJRPFlIzxsFyliYB\nIMW5+kPL3d4x7CF2XTVSBdm0kzaViOY1bmLPqwGHzD1e1kz1Q9oSpdNGvOtp6EwL\n8ccJV2Wo0hPCRuPItCNL/pWVEiyKCNjKdsjOGZtzdedHdmIjS3hv8GogQO0SVxjp\nn72h90dxVw8IQEpJJkdZKzBVFPnhGSDhxdudTzNso6Txb5xQHpXa5MIHBwbCZRF9\nmUt/dab9AgMBAAECggEADh+OpGjplJgNzJMg3VOk3NyoeF8wScq3xpI/u7ZAALOV\n5X1UPyttAlXaHsqCk3sj3VNokRIZX2TscjVbauRI2Pg/oqHppScvlpthrky6gnbA\n11NDxWoFCCzii2jOUpJK8596rgFhUt0T/MslyaFScwGQDrk5neX7dskI2z2vzWtq\nLX5z/PoUOIt+HvsL0LY0wT9n6GwSjI3liUZoytCnEPfl6StZWDkAmaTF/mirQOP/\naw1hXNTTrIF0ZPXEen9/orNt2rhmRge3K0jqIMvnHMqHHyTVo6CAZmnwKuN5ugTW\nsBlwguVYgJDHbKeGLmX+/9pFzpxM2+n2SfiSn1mKgQKBgQDX2Jz98NbB2BBSzBQD\nyBsBugYxhH0aPweKRLiJMFsDP1vlL14D0SLoGaPWyI5rNTRUMydgvMKvGwEVuC88\nlEjUWJehZIhOnQvBJSPLZbeN3d2kQ4Z4Rnb3i05v2HPSAtztApThTXjWJNQYyfJB\nzULTdg5KtsHCDG+z/nJJlPQUfQKBgQC1nBhXzC5qdJ0m6ejoZ4zAhpwWyAU517ws\nMBuPuS7JckL0AqxKnSpY89mcpVVSPiFMJVpLVZcl4t0nbfZP7hFSCeXPWCISnmra\nnvJ9ZCGo4bNrkNvLfXbjhEjeu46G72/6cmBKHksAt0xCqvhLV58QfA4+8xgiYxB4\nw0pCtJjkgQKBgEPyveE3KvQU53aZJgfWu6G8hOybr6JOizoczhbp8QzBqlUopyj+\nckWspKYdtq/LLPEAtXm/km37S0kiFUS1zYODbCBzfHF7ANNJtM339GOln3txgmhk\njlj5MrUE59kJ67B06pdOgyauq1IuaKQMUOgutusQQ0iqD5QTGrlNOdUlAoGBAIWq\nuhAE7DTWV8SIbTCA5ovdh40M8yu7qXgsgFysQ89pFfZa8UyJmN2XvRcaaU37BK7y\n3x6LhJASBgw7VwtFgeIL/uU5TPq/No5qZrf7tvqCBHirSdrgIV0bxDaLfT+7g4Om\nI1DqMvH3910qUU3C1ARiCmoyqhTFLR51PncSTWYBAoGAVF/lTsQpHfxDHBs0D9fM\nq9GdmNvtkCzKxq1vBkEbJy1sdkondF3caRyM5vtc9xOgLpLaxgO8QMByJ32J6oXU\nnwo3wXuFrZXrzk0yBza0q+1X5ebqOeCMDm/WcL6YmWF2mN49VERi0rJ/YYFHHiim\nUvKtS5qqDTnfvZx8YfSLsjA=\n-----END PRIVATE KEY-----\n",
              "client_email": "speech-recog@glassy-strata-278319.iam.gserviceaccount.com",
              "client_id": "100621716077963145382",
              "auth_uri": "https://accounts.google.com/o/oauth2/auth",
              "token_uri": "https://oauth2.googleapis.com/token",
              "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
              "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/speech-recog%40glassy-strata-278319.iam.gserviceaccount.com"
            }
        """
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
