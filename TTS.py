#importing the module
from modules import *

#the graphical user UI , overall
root = Tk()
root.geometry("400x400")
root.title("Text to Speech")
root.config(bg="white")

Label(root, text="Text to Speech", bg="white smoke").pack()
Label(root, text="Enter text:", bg="white smoke").place(x=20, y=60)


#to read the text on the typing box
Msg = StringVar()

#the typing box itself
input_field = Entry(root, textvariable=Msg, width="40")
input_field.place(x=20, y=100)

#TTS functions
def tts():
    message = input_field.get()
    speech = gTTS(text=message)
    speech.save("speech.mp3")
    playsound("speech.mp3")
#for exit  button
def Exit():
    root.destroy()
#for reseting the text boxes
def Reset():
    Msg.set("")

#buttons and its command
Button(root, text="Play", command=tts, width=3).place(x=20, y=140)
Button(root, text="Exit", command=Exit, width=3).place(x=80, y=140)
Button(root, text="Reset", command=Reset, width=3).place(x=140, y=140)

#to make sure the window not close after 0.01 nanosecond when running the application
root.mainloop()
