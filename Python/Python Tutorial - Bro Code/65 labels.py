from tkinter import *

window = Tk()

# Check documentation for additional label formatting options
label = Label(window,
              text="Hello World",
              font=('Arial',20,'bold'),
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20)
label.place(x=0,y=0)

window.mainloop()