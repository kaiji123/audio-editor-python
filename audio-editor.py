import librosa
import numpy as np

import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def remove_silence(input_file, output_file, min_silence_len=500, silence_threshold=-40):
    # Extract audio from video
    print(input_file)
    audio = AudioSegment.from_file(input_file, format='m4a')
    
    # Split audio on silence
    chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_threshold)
    
    # Concatenate non-silent chunks
    non_silent_audio = chunks[0]
    for chunk in chunks[1:]:
        non_silent_audio += chunk
    
    # Export the modified audio to a new file
    non_silent_audio.export(output_file, format=os.path.splitext(output_file)[1][1:])



def speed_up_audio(input_file, output_file, speed_factor=1.5):
    # Load the input audio file
    audio = AudioSegment.from_file(input_file)

    # Apply speed up effect
    sped_up_audio = audio.speedup(playback_speed=speed_factor)

    # Export the sped up audio to a new file
    sped_up_audio.export(output_file, format='wav')




# removing silence from all the files in current directory
current_directory = os.getcwd()
for file_name in os.listdir(current_directory):
    if file_name.endswith('.m4a'): # change it to your own format
        # Construct the input and output file paths
        input_file = os.path.join(current_directory, file_name)
        output_file = os.path.join(current_directory, 'no_silence_' + file_name.split(".")[0]+".wav")

        # Remove silence from the audio file
        remove_silence(input_file, output_file)

