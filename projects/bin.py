from tkinter import *
def submit():
    print(f"the tempreture is {scale.get()} degres celcius.")
window=Tk()
# fire=PhotoImage(file="img.png")
# label=Label(window,image=fire)
# label.pack()
scale=Scale(window,
            from_=100,
            to_=0,
            font=('consolas',15),
            length=300,
            tickinterval=10,
            resolution=5,
            troughcolor="#69EAFF",
            fg="red",
            bg="#111111")
button=Button(window,text="submit",command=submit)

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()
button.pack()
# ice=PhotoImage(file='img.png')
# label_2=Label(window,image=ice)
# label_2.pack()

window.mainloop()