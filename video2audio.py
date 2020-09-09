from tkinter import messagebox,filedialog
import tkinter as tk
from tkinter import *
from moviepy.editor import *
import sys, errno

root=tk.Tk()
root.geometry("400x200")
root.config(bg="#3E4652")
root.title("Video to Audio Convertor | Manjunathan C")
root.iconphoto(False,tk.PhotoImage(file="icon.png"))

def open():
	try:
		vid=filedialog.askopenfilename(title="Select Video file",filetypes=(('MP4','*.mp4'),('MKV','*.mkv'),('WEBM','*.webm'),('AVI','*.avi'),))
		video=VideoFileClip(vid)
		audio = video.audio
		a= filedialog.asksaveasfile(defaultextension='.mp3',filetypes=(('mp3','*.mp3'),))
		messagebox.showinfo("File","Choose the saved Audio File")
		def aud():
			try:
				b=filedialog.askopenfilename(title="Select audio file",filetypes=(('mp3','*.mp3'),))
				x=audio.write_audiofile(b)
				messagebox.showinfo("Process","Successful")
			except:
				messagebox.showerror("File","You must Choose the saved Audio File")
				aud()
		aud()
	except:
		messagebox.showerror("Error","Unknown Error Occured")
	
	
	

label=Label(root,text="Video to Audio Convertor",bg="#3E4652",fg="#25C831",font=("fontawesome",15,"bold italic")).place(x=60,y=0)
button=Button(root,text="Choose file",bg="#0C897C",fg="white",font=("fontawesome",15,"bold italic"),command=open).place(x=120,y=50)
button1=Button(root,text="Quit",bg="#0C897C",fg="white",font=("fontawesome",15,"bold italic"),command=root.quit).place(x=160,y=110)

root.mainloop()