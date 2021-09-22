from tkinter import *
root = Tk()
root.title("First GUI")
myText = Label(text="My Name Is",fg="red",font=20).grid(row=0,column=0)
myText = Label(text="Arachaporn",fg="pink",font=20).grid(row=1,column=1)
myText = Label(text="Ngammungsakul",fg="blue",font=20).grid(row=2,column=2)
root.geometry("300x300")
root.mainloop()