"""
Widgets = GUI elements: buttons, textboxes, labels, images
Windows = Serves as a container to hold or contain those widgets
"""

import tkinter

window = tkinter.Tk() # Instantiate an instance of a window
window.geometry("1024x1024")
window.title("Jason Clishe")
window.config(background="white")


window.mainloop() # Place a window on computer screen, listen for events