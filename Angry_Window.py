from tkinter import *
import time
# Blank window.
root = Tk()
root.geometry("100x100")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

eyes = Label(topFrame, text="＼(^o^)／")
eyes.pack(side="bottom")

variable=StringVar()

random_text = ["＼(^o^)／", "¯\_(ツ)_/¯", "\ (•◡•) /", "~(˘▾˘~)", ":')" ]

def update_label():
    i = 0
    while 1:
        time.sleep(1)
        if (i >= 4):
            i = 0
        variable.set(str(random_text[i]))
        i += 1
        root.update()

your_label=Label(root, textvariable = variable)
your_label.pack()
start_button=Button(root, text = "start", command = update_label)
start_button.pack()

# Keep running window
root.mainloop()
