import sys
from moviepy.editor import *
a=input("enter the file path : ")
video = VideoFileClip(a) 
audio = video.audio 
b=input("enter the audio path : ")
audio.write_audiofile(b) 
