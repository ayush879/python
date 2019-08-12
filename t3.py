from tkinter import *
from tkinter import messagebox
top=Tk()
def helloCallBack():
    messagebox.showinfo("hello python","hello world")
b=Button(top,text="hello",activebackground="red",
activeforeground="yellow",command=helloCallBack)
b.pack()
top.mainloop()