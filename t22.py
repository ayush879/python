import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
canvas1=tk.Canvas(root,width=800,height=350)
canvas1.pack()
def ExitApplication():
    MsgBox=tk.messagebox.askquestion('exit application','are you sure you wnat to exit the application',icon='warning')
    if MsgBox=='yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('return','you will now return to the application screen')
button1=tk.Button(root,text='exit application',command=ExitApplication)
canvas1.create_window(97,270,window=button1)
root.mainloop()