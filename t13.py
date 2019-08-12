from tkinter import *
canvas_width=600
canvas_height=600
master=Tk()
canvas=Canvas(master,width=canvas_width,height=canvas_height)
canvas.pack()
img=PhotoImage(file="mat.png")
canvas.create_image(10,10,anchor=NW,image=img)
mainloop()