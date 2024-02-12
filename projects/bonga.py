from tkinter import *

def backspace():
    entry.delete(len(entry.get())-1,END)
def delete():
    entry.delete(0,END)

def submit():
    user_name=entry.get()
    print(f"hello {user_name}")
window= Tk()


entry=Entry(window,
            font=("Arial",40,),
            fg="green",bg="black",show="")
entry.insert(0,"NAME")
submit_button=Button(window,text="submit" ,command=submit)


delete_button=Button(window,text="delete" ,command=delete)
backspace_button=Button(window,text="backspace",command=backspace)

backspace_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
submit_button.pack(side=RIGHT)
entry.pack(side=LEFT)
window.mainloop()