from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv

window = Tk()
window.geometry("610x710+410+15")
window.title("Voice Recorder")
window.configure(background="grey")

def fun_rec():
    
    freq = 44100
    file_temp = file_name.get()
    dur = int(time_dur.get())
    recording = sound.rec(dur*freq, samplerate=freq, channels=2)
    try :
        my_temp = int(time_dur.get())
    except:
        print("Do Print the correct value")

    while my_temp>0:
        window.update()
        time.sleep(1)
        my_temp = my_temp-1

        if my_temp ==0 :
            messagebox.showinfo("Time countdown here", "time up")
            
        Label(text=f"{str(my_temp)}", font="Arial 40", width=4, background="grey").place(x=250, y=600)
        
    sound.wait()
    write(f"{file_temp}.wav", freq, recording)
    

icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)

show_img = PhotoImage(file="icon.png")
my_image = Label(image=show_img, background="grey")
my_image.pack(padx=15, pady=15)

Label(text="Voice Recorder", font=("Arial", 25, "bold"), background="grey", fg="black").pack()

time_dur = StringVar()
time_entry = Entry(window, textvariable=time_dur, font=("Arial", 25, "bold"), width=15).pack(pady=5)
Label(text="Enter the time in seconds", font=("Arial" , 12, "bold"), background="grey", fg="black", pady=10).pack()

file_name = StringVar()
file_entry = Entry(window, textvariable=file_name, font=("Arial", 25, "bold"), width=15).pack(pady=5)  
Label(text="Enter file name to save recording", font=("Arial" , 12, "bold"), background="grey", fg="black", pady=10).pack()

record_bt = Button(window , font=("Arial", 20 , "bold"), text="Record", bg="grey", fg="black", borderwidth=1, command=fun_rec , pady=2, padx=2).pack()

    
window.mainloop()
