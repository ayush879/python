from tkinter import *
from tkinter import messagebox
top=Tk()
CheckVar1=IntVar()
CheckVar2=IntVar()
c1=Checkbutton(top,text="Music",onvalue=1,offvalue=0,height=5,width=20)
c2=Checkbutton(top,text="vedio",onvalue=1,offvalue=0,height=5,width=20)
c1.pack()
c2.pack()
top.mainloop()