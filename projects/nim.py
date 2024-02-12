from tkinter import *

count=0
def click():
    global count 
    count+=1
    print(count)

windows=Tk()
windows.title("my first ever GUI")
windows.geometry("500x500")
windows.config(background="white")
button=Button(windows,text="click me ",
            font=('Arial',23),
            bg="black",
            fg="green",
            relief=RAISED,
            bd=10,
            padx="10",
            pady="10",
            command=click,
            )
button.pack()



windows.mainloop()