from tkinter import *

def show():
    lb.config(text = 'Button was clicked!!')

root = Tk()
root.title('Welcome to MCA App')
lb = Label(root, text = 'Hello', )
lb.pack(side = LEFT)
b = Button(root, text = 'Click Me', command = show)
b.pack(side = LEFT)
mainloop()