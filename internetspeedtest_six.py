# calculating download and upload speed

from tkinter import *        # for graphics
import speedtest           # for internet speed, pip install speedtest-cli will work but not pip install speedtest

# function to check the net speed
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str( round((sp.download())/(10**6),3)) + " Mbps" # speed is in bits so convert into Mbps and round the numbers
    up = str( round(sp.upload()/(10**6),3)) + " Mbps"
    label_down.config(text=down)    # replace download label text with 00
    label_up.config(text=up)        # replace upload label text with 00

sp = Tk()   # create object of tkinter for GUI

sp.title(" Internet Speed ")        # window title
sp.geometry("500x600")              # window size
sp.config(bg="Blue")                # window background color

# labels for user information/download/upload speed
label = Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
label.place(x=60,y=40,height=50,width=380)

label = Label(sp,text="Download Speed",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
label.place(x=60,y=130,height=50,width=380)

label_down = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
label_down.place(x=60,y=200,height=50,width=380)

label = Label(sp,text="Upload Speed",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
label.place(x=60,y=290,height=50,width=380)

label_up = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
label_up.place(x=60,y=360,height=50,width=380)

# Button to check the net speed
button = Button(sp,text="Check Speed",font=("Time New Roman",30,"bold"),relief="raised",command=speedcheck)
button.place(x=60,y=430,height=50,width=380)



sp.mainloop()



