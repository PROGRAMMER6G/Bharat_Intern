from tkinter import *
import math
import tkinter.messagebox
root=Tk()
root.geometry("540x460")
root.title("Calculator")
switch=None
def btn_1():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'7')
def btn_2():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'8')
def btn_3():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'9')
def btn_4():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'4')
def btn_5():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'5')
def btn_6():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'6')
def btn_7():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'1')
def btn_8():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'2')
def btn_9():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'3')
def btn_0():
    if disp.get()=='0':
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,'0')

def btn_p():
    pos=len(disp.get())
    disp.insert(pos,'+')
def btn_s():
    pos=len(disp.get())
    disp.insert(pos,'-')
def btn_m():
    pos=len(disp.get())
    disp.insert(pos,'*')
def btn_d():
    pos=len(disp.get())
    disp.insert(pos,'/')

def btn_dot():
    pos=len(disp.get())
    disp.insert(pos,'.')
def btn_bl():
    pos=len(disp.get())
    disp.insert(pos,'(')
def btn_br():
    pos=len(disp.get())
    disp.insert(pos,')')
def btn_c():
    pos=len(disp.get())
    disp.delete(0,END)
def btn_eq():
    try:
        ans=disp.get()
        ans=eval(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except Exception:
        tkinter.messagebox.showerror("Value error! Check operator or operand")
def back():
    pos=len(disp.get())
    display=str(disp.get())
    if display=="":
        disp.insert(0,'0')
    elif display=='':
        disp.insert(0,'0')
    elif display=='0':
        pass
    else:
        disp.delete(0,END)
        disp.insert(0,display[0:pos-1])

disp=Entry(root,font="Verdana 40",fg="white",bg="#151B54",bd=1,justify=RIGHT)
disp.insert(0,'0')
disp.pack(expand=TRUE, fill=BOTH)
btnrow1=Frame(root,bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)
C_btn=Button(btnrow1,text="C",font="Segoe 21",relief=GROOVE,bd=0,command=btn_c,fg="white",bg="maroon").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn1=Button(btnrow1,text="7",font="Segoe 23",relief=GROOVE,bd=0,command=btn_1,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn2=Button(btnrow1,text="8",font="Segoe 23",relief=GROOVE,bd=0,command=btn_2,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn3=Button(btnrow1,text="9",font="Segoe 23",relief=GROOVE,bd=0,command=btn_3,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
plsbtn=Button(btnrow1,text="+",font="Segoe 23",relief=GROOVE,bd=0,command=btn_p,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)

btnrow2=Frame(root,bg="#000000")
btnrow2.pack(expand=TRUE, fill=BOTH)
btnb=Button(btnrow2,text="⌫",font="Segoe 15",relief=GROOVE,bd=0,command=back,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn4=Button(btnrow2,text="4",font="Segoe 23",relief=GROOVE,bd=0,command=btn_4,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn5=Button(btnrow2,text="5",font="Segoe 23",relief=GROOVE,bd=0,command=btn_5,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn6=Button(btnrow2,text="6",font="Segoe 23",relief=GROOVE,bd=0,command=btn_6,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
plsbtn=Button(btnrow2,text="-",font="Segoe 27",relief=GROOVE,bd=0,command=btn_s,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)

btnrow3=Frame(root,bg="#000000")
btnrow3.pack(expand=TRUE, fill=BOTH)
sin_btn=Button(btnrow3,text="(",font="Segoe 27",relief=GROOVE,bd=0,command=btn_bl,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn7=Button(btnrow3,text="1",font="Segoe 24",relief=GROOVE,bd=0,command=btn_7,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn8=Button(btnrow3,text="2",font="Segoe 23",relief=GROOVE,bd=0,command=btn_8,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn9=Button(btnrow3,text="3",font="Segoe 23",relief=GROOVE,bd=0,command=btn_9,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
plsbtn=Button(btnrow3,text="*",font="Segoe 27",relief=GROOVE,bd=0,command=btn_m,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)

btnrow4=Frame(root,bg="#000000")
btnrow4.pack(expand=TRUE, fill=BOTH)
sin_btn=Button(btnrow4,text=")",font="Segoe 25",relief=GROOVE,bd=0,command=btn_br,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)
cos_btn=Button(btnrow4,text=".",font="Segoe 21",relief=GROOVE,bd=0,command=btn_dot,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)
btn0=Button(btnrow4,text="0",font="Segoe 23",relief=GROOVE,bd=0,command=btn_0,fg="black",bg="#368BC1").pack(side=LEFT,expand=TRUE,fill=BOTH)
btne=Button(btnrow4,text="=",font="Segoe 23",relief=GROOVE,bd=0,command=btn_eq,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)
plsbtn=Button(btnrow4,text="/",font="Segoe 26",relief=GROOVE,bd=0,command=btn_d,fg="white",bg="#123456").pack(side=LEFT,expand=TRUE,fill=BOTH)

root.mainloop()
