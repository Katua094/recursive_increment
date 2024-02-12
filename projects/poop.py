from tkinter import *


def display():
    if x.get()==1:
        print("you agree")
    else:
        print("you disagree")
window= Tk()
x= BooleanVar()

image= PhotoImage(file="img.png")
check_box=Checkbutton(window,
                      text="do you agree",
                      variable=x,
                      onvalue=True,
                      offvalue=False,
                      font=("Arial",20,),
                      fg="#00ff00",
                      bg="black",
                      command=display,
                      compound=LEFT,
                      activebackground="black",
                      activeforeground="#00ff00")
check_box.pack()
window.mainloop()