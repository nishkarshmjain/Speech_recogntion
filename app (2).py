# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:18:11 2020

@author: nish
"""

import speech_recognition as sr
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import moviepy.editor as mp 




def video_to_audio(video_path) :
    clip = mp.VideoFileClip(video_path) 
    clip.audio.write_audiofile(r"C:\Users\nish\Desktop\Projects\Spyder Projects\SPeechRecognition\audio2.wav") 
    audio_path = r"C:\Users\nish\Desktop\Projects\Spyder Projects\SPeechRecognition\audio2.wav"
    return audio_path


r = sr.Recognizer()

def microphone_recognition() : 
    with sr.Microphone() as source:
        print("Speak")
        audio_data = r.record(source, duration=15)
        print("Converting to text")
        text = r.recognize_google(audio_data, language="en-IN")
        print(text)





def video_audio_transcription(path):

    sound = AudioSegment.from_wav(path)  
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-14,
        keep_silence=500,
    )
    audio_chunks_path = r"C:\Users\nish\Desktop\Projects\Spyder Projects\SPeechRecognition\audio-chunks"
    
    if not os.path.isdir(audio_chunks_path):
        os.mkdir(audio_chunks_path)
    whole_text = ""
    
    for i, audio_chunk in enumerate(chunks, start=1):

        chunk_filename = os.path.join(audio_chunks_path, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        
        with sr.AudioFile(chunk_filename) as source:
            audio = r.record(source)
            
            try:
                text = r.recognize_google(audio,language="en-IN")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
                
                
    return whole_text


#if __name__ == '__main__':

    #audio_path = r"C:\Users\nish\Desktop\Projects\Spyder Projects\SPeechRecognition\audio2.wav"
    #video_path= r"C:\Users\nish\Desktop\Projects\Spyder Projects\SPeechRecognition\sample2.mkv"
    #audio_path = video_to_audio(video_path)
    
print("\nFull text:", video_audio_transcription(r"C:\Users\nish\Desktop\Projects\Spyder Projects\SPeechRecognition\audio2.wav"))

