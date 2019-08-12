from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry("100x100")
def hello():
    messagebox.showinfo("say hello","hello world") 
b1=Button(top,text="say hello",command=hello)
b1.place(x=35,y=50)
top.mainloop()