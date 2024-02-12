from tkinter import *

food=["pizza","hamburger","chapati"]
def order():
    if (x.get()==0):
        print("you choosed pizza")
    elif (x.get()==1):
        print("you ordered a hamburger")
    elif (x.get()==2):
        print("you ordered chapati fam")

window=Tk()
x=IntVar()
for index in range(len(food)):
    radio_button=Radiobutton(window,
                             text=food[index],
                             variable=x,
                             value=index,
                             padx=10,
                             pady=10,
                             font=('Arial',50),
                             indicatoron=0,
                             width=20,
                             command=order,
                             bg="black",
                             fg="#00ff00",
                             activebackground="black",
                             activeforeground="#00ff00"
                             

                             )
    radio_button.pack(anchor=W)


window.mainloop()