from tkinter import *
import time
import random
import sys

# Blank window.
root = Tk()
root.title("Evil_Window")
root.geometry("100x100")
root.configure(bg="#0e4f73")
root.config(highlightbackground="white", highlightcolor="white", highlightthickness=3)
root.overrideredirect(True)
# Fixed window dimensions. Disables maximise button.
root.resizable(width=False, height=False)

def close(event):
    root.destroy()
root.bind('<Escape>', close)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

topFrame = Frame(root)
topFrame.pack()

x = (screen_width/2) - (100/2)
y = (screen_height/2) - (100/2)
root.geometry('%dx%d+%d+%d' % (100, 100, x, y))

face_holder = StringVar()

random_faces = ["＼(^o^)／", "¯\_(ツ)_/¯", "\ (•◡•) /", "~(˘▾˘~)", "ヽ(•‿•)ノ", "(ﾉ^_^)ﾉ"]

def update_label():
    i = random.randrange(6)
    face_holder.set(str(random_faces[i]))
    root.update()

def update_pos():
    random_option = random.randrange(4)
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    print("Update_Pos", random_option)
    if (random_option == 0):
        current_x += 5
        current_y += 5
    if (random_option == 1):
        current_x -= 5
        current_y -= 5
    if (random_option == 2):
        current_x += 5
        current_y -= 5
    if (random_option == 3):
        current_x -= 5
        current_y += 5
    print(current_x, current_y)
    root.geometry("100x100" + "+" + str(current_x) + "+" + str(current_y))
    if (current_x >= screen_width):
        root.geometry("100x100" + "+" + str(-root.winfo_x()) + "+" + str(-root.winfo_x()))
    if (current_y >= screen_height or current_y <= 0):
        root.geometry("100x100" + "+" + str(-root.winfo_x()) + "+" + str(-root.winfo_x()))
    root.update()

face = Label(root, textvariable=face_holder)
face.place(relx=.5, rely=.5, anchor="center")
"""
start_button = Button(root, text="start", command=update_label)
start_button.pack()
"""

def current_pos():
    current_x1 = root.winfo_x()
    current_y2 = root.winfo_y()
    if (current_x1 != root.winfo_x() or current_y2 != root.winfo_y):
        print("Current_Cord")
        print("x", current_x1)
        print("y", current_y2)
    else:
        pass

"""
start_button2 = Button(root, text="Start", command=update_pos)
start_button2.pack()

current_cord_button = Button(root, text="Current_Cord", command=current_pos)
current_cord_button.pack()
"""
current_x1 = root.winfo_x()
current_y2 = root.winfo_y

while True:
    internal_option = random.randrange(2)
    print("Internal_Option:", internal_option)
    if (internal_option == 0):
        for i in range(20):
        #    time.sleep(0.1)
            update_pos()
    if (internal_option == 1):
        update_label()
        time.sleep(0.1)

# Keep running window
root.mainloop()

