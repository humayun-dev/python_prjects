from tkinter import *
import os

# functions call for restart,shutdown,restart with time and log out
def restart():
    os.system("shutdown /r /t 1")   # 1 = 1 sec time
def shutdown():
    os.system("shutdown /s /t 1")
def shutdownwithtime():
    os.system("shutdown /r /t 20")  # 20 = 20 sec time
def logout():
    os.system("shutdown -l")

st = Tk()   # object of tkinter for GUI, all code should be within object and mainloop()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="grey")

# Create button by using Button() class object and few characteristics
r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,width=200,height=50)

# Restart with time button
rt_button = Button(st,text=("Restart Time"),font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdownwithtime)
rt_button.place(x=150,y=170,width=200,height=50)

# Log Out button
lg_button = Button(st,text=("Log Out"),font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,width=200,height=50)

# Shut Down button
st_button = Button(st,text=("Shut Down"),font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,width=200,height=50)

st.mainloop()

