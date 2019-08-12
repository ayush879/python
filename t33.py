from tkinter import filedialog
from tkinter import *
root=Tk()
root.filename=filedialog.asksaveasfilename(initialdir="/",title="select file",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
print(root.filename)
mainloop()