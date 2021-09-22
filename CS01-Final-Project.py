from tkinter import *
root = Tk()
root.title("First GUI")

content = ""
txt_input = StringVar(value="0" )

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = ""

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,'0')

display = Entry(font=('arial',25,'bold'),fg="black",bg="white",textvariable=txt_input,justify="right")
display.grid(columnspan=4)

#row1
btn7=Button(fg='purple',bg='white',font=('arial',25,'bold'),text="7",command=lambda:btn(7),padx=20,pady=10).grid(row=1,column=0)
btn8=Button(fg='purple',bg='white',font=('arial',25,'bold'),text="8",command=lambda:btn(8),padx=20,pady=10).grid(row=1,column=1)
btn9=Button(fg='purple',bg='white',font=('arial',25,'bold'),text="9",command=lambda:btn(9),padx=20,pady=10).grid(row=1,column=2)
btnc=Button(fg='white',bg='pink',font=('arial',25,'bold'),command=clear,text="c",padx=20,pady=10).grid(row=1,column=3)

#row2
btn4=Button(fg='blue',bg='white',font=('arial',25,'bold'),text="4",command=lambda:btn(4),padx=20,pady=10).grid(row=2,column=0)
btn5=Button(fg='blue',bg='white',font=('arial',25,'bold'),text="5",command=lambda:btn(5),padx=20,pady=10).grid(row=2,column=1)
btn6=Button(fg='blue',bg='white',font=('arial',25,'bold'),text="6",command=lambda:btn(6),padx=20,pady=10).grid(row=2,column=2)
btnplus=Button(fg='white',bg='violet',font=('arial',25,'bold'),text="+",padx=20,command=lambda:btn("+"),pady=10).grid(row=2,column=3)

#row3
btn1=Button(fg='cyan',bg='white',font=('arial',25,'bold'),text="1",command=lambda:btn(1),padx=20,pady=10).grid(row=3,column=0)
btn2=Button(fg='cyan',bg='white',font=('arial',25,'bold'),text="2",command=lambda:btn(2),padx=20,pady=10).grid(row=3,column=1)
btn3=Button(fg='cyan',bg='white',font=('arial',25,'bold'),text="3",command=lambda:btn(3),padx=20,pady=10).grid(row=3,column=2)
btnminus=Button(fg='white',bg='violet',font=('arial',25,'bold'),text="-",command=lambda:btn("-"),padx=24,pady=10).grid(row=3,column=3)

#row4
btndot=Button(fg='lime',bg='white',font=('arial',25,'bold'),text=".",command=lambda:btn("."),padx=24,pady=10).grid(row=4,column=0)
btn0 =Button(fg='lime',bg='white',font=('arial',25,'bold'),text="0",command=lambda:btn(0),padx=20,pady=10).grid(row=4,column=1)
btnvisiob=Button(fg='lime',bg='white',font=('arial',25,'bold'),command=lambda:btn("/"),text="/",padx=24,pady=10).grid(row=4,column=2)
btnmultiply=Button(fg='white',bg='violet',font=('arial',25,'bold'),text="x",command=lambda:btn("*"),padx=20,pady=10).grid(row=4,column=3)

#row5
btnequal=Button(fg='white',bg='pink',font=('arial',25,'bold'),text="=",command=equal,padx=64,pady=10).grid(row=5,column=0,columnspan=2)
btnopen=Button(fg='white',bg='violet',font=('arial',25,'bold'),text="(",command=lambda:btn("("),padx=23,pady=10).grid(row=5,column=2)
btnclose=Button(fg='white',bg='violet',font=('arial',25,'bold'),text=")",command=lambda:btn(")"),padx=24,pady=10).grid(row=5,column=3)

root.mainloop()