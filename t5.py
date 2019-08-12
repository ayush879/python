from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
canvas.create_line(0,0,500,500)
mainloop()
import tkinter 
top=Tk()
c=Canvas(top,bg="lavender",height=250,width=300)
coord=10,50,240,210
arc=c.create_arc(coord,start=0,extent=150,fill="pink")
c.pack()
top.mainloop()
