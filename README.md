
# Speech To Text Transcription

This program makes use of the following libraries:
* [Pydub](https://pypi.org/project/pydub/)
* [Speech Recognition](https://pypi.org/project/SpeechRecognition/)
* [Noise Reduce](https://pypi.org/project/noisereduce/)

This Python project is for my own personal use. It is meant to take video or audio and convert it into text. There are 3 tools, and in addition there is a pipe and a audio converter class.

#### Tools:
* `Extract_Audio`
    * The purpose of this module is simply to save the the audio from a video in `wav` format.
* `Denoise`
    * The purpose of this module is to take audio with noise, and eliminate it.
* `Speech_To_Text`
    * The purpose of this module is to take the audio file and create a text file, currently the conversion is done with google's speech to text api.

#### Audio converter class: `Audio_Converter`
The purpose of this module is to take all the available tools and and streamline the process of conversion.

#### Pipe: `Audio_Conversion_Pipe` 
Like the previous module, the audio converter, this is also meant to streamline the process of conversion.
First you initialize it with a list containing every class you want to iterate through, this will be the pipe.
After when the method `run` is called. The parameter for `run` is `first_arg`, meant to serve as the input for the first call of the pipe that gets iterated through.

## This is a work in progress and is not complete, as there are numerous issues with the available speech transcription services.