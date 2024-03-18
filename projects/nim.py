from tkinter import *

def submit():
    input_text = text.get("1.0", END)
    print(input_text)

windows = Tk()

text = Text(windows,
            bg='light yellow',
            fg='black',
            font=('inkfree',12),
            height=8,
            width=20,
            padx=20,
            pady=20,
            )  # Fixed the font name
text.pack()

button = Button(windows, text="submit", command=submit, font=('Arial', 15))
button.pack()

windows.mainloop()
