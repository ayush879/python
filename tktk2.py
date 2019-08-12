from tkinter import *
from tkinter import messagebox
#wind=Tk()
#wind.mainloop()
#root=Tk()
#label=Label(root,text='how are you going',relief=RIDGE,bg='blue',cursor='spider',bd='4',font='Arial',width=30,
#underline=15,fg='yellow')
#label.pack()
#root.mainloop()
#top=Tk()
#def helloCallBack():
 #   messagebox.showinfo("hello python","hello world")
#B=Button(top,image="wall7.jpg",activebackground="red",activeforeground="yellow",command=helloCallBack)
#B.pack()
#top.mainloop()
#c1=Checkbutton(top,text="music",onvalue=1,offvalue=0,height=5,width=20)
#c2=Checkbutton(top,text="video",onvalue=1,offvalue=0,height=5,width=20,state=DISABLED)
#c1.pack()
#c2.pack()
#top.mainloop()
top=Tk()
c=Canvas(top,bg="lavender",height=450,width=500)
#coord=10,50,220,240
#arc=c.create_arc(coord,start=0,extent=359,fill="pink")
#line=c.create_line(20,80,80,40,120,80)
#oval=c.create_oval(10,20,150,100)
polygon=c.create_polygon(20,50,40,50,40,20,60,20,60,50,80,50,80,70,20,70)
c.pack()
top.mainloop()