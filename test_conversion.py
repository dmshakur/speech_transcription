from optparse import OptionParser
from audio_converter import transcription_tools.Audio_Converter

if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option(
        '-a',
        '--afp',
        dest = 'audio_file_path',
        action = 'store',
        type = 'string'
        )
    parser.add_option(
        '-v',
        '--vfp',
        dest = 'video_file_path',
        action = 'store',
        type = 'string'
        )
    parser.add_option(
        '-t',
        '--tfp',
        dest = 'text_file_path',
        action = 'store',
        type = 'string'
        )
    parser.add_option(
        '-b',
        '--verbose',
        dest = 'verbose',
        action = 'store_true',
        default = False
        )
    parser.add_option(
        '-q',
        '--quiet',
        dest = 'verbose',
        action = 'store_false',
        )
    parser.add_option(
        '-d',
        '--denoise_args',
        dest = 'denoiser_arguments',
        default = None,
        type = 'string'
    )
    
    options, args = parser.parse_args()

    if 3 <= len(args) <= 5:
        parser.error('Incorrect number of arguments')

    if options.verbose:
        print('arguments verified')
        print('beginning audio processing process')
        print('initializing converter')

    audio_conv = Audio_Converter(
        vfp = options.video_file_path,
        afp = options.audio_file_path,
        tfp = options.text_file_path,
        dargs = options.denoiser_arguments,
        v = options.verbose
    )

    if options.verbose: print('converting audio file')
    
    output = audio_conv.run()
else: print('This script is meant to be run from the terminal only.')