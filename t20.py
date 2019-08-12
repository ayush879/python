import sys
from tkinter import *
from tkinter import messagebox
def answer():
    showerror("answer","sorry,no answer avaliable")
def callback():
    if askyesno('verify','really quit?'):
        showwarning('yes','not yet implemented')
    else:
        showinfo('no','quit has been cancelled')
Button(text='quit',command=callback).pack(fill=X)
Button(text='answer',command=answer).pack(fill=X)
mainloop()
