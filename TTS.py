#importing the modules
from tkinter import *
from gtts import gTTS
 
import os
 

root = Tk()
 
#yellow upper part of app
frame1 = Frame(root,
               bg = "yellow",
               height = "150")
 
#filling it with colour
frame1.pack(fill = X)
 
#ditto as 1 but lower part
frame2 = Frame(root,
               bg = "red",
               height = "750")
frame2.pack(fill=X)
 
 
 
#app title on upper section
label = Label(frame1, text = "Text to Speech",
              font = "bold, 30",
              bg = "cyan")
 
label.place(x = 180, y = 70)
 
 
 
entry = Entry(frame2, width = 45,
              bd = 4, font = 14)
 
entry.place(x = 130, y = 52)
entry.insert(0, "")
 
#playing the sound
def play():
    #which language for TTS used
    language = "en"
 
 
 
     #passing the language 
    obyek = gTTS(text = entry.get(),
                lang = language,
                slow = False)
 
 
 

    obyek.save("TTS.wav")
    os.system("TTS.wav")
 
#submit button to play
btn = Button(frame2, text = "SUBMIT",
             width = "15", pady = 10,
             font = "bold, 15",
             command = play, bg='yellow')
 
btn.place(x = 250,
          y = 130)
 
root.title("TTS") #App name on window bar

 
root.geometry("650x550+350+200")
 
root.mainloop()