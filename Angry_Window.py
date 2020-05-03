""" ---

---

"""

__author__ = 'Anthony T Nguyen'
__version__ = ''
__date__ = ''
__status__ = 'Development'

from tkinter import *
import time
import random
import sys

random_faces = ["＼(^o^)／", "¯\_(ツ)_/¯", "\ (•◡•) /", "~(˘▾˘~)", "ヽ(•‿•)ノ", "(ﾉ^_^)ﾉ", "ʕっ•ᴥ•ʔっ"]
# Blank window.
root = Tk()
root.title("Angry_Window")
root.geometry("100x100")
root.configure(bg="#0e4f73")
root.config(highlightbackground="white", highlightcolor="white", highlightthickness=3)
root.overrideredirect(True)
# Fixed window dimensions. Disables maximise button.
root.resizable(width=False, height=False)
root.lift()
root.attributes("-topmost", True)

def close(event):
    root.destroy()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

topFrame = Frame(root)
topFrame.pack()

face_holder = StringVar()
face = Label(root, textvariable=face_holder, font='TkDefaultFont 12 bold')
face.place(relx=.5, rely=.5, anchor="center")
"""
start_button = Button(root, text="start", command=update_label)
start_button.pack()
"""

"""
start_button2 = Button(root, text="Start", command=update_pos)
start_button2.pack()

current_cord_button = Button(root, text="Current_Cord", command=show_current_pos)
current_cord_button.pack()
"""
x = (screen_width/2) - (100/2)
y = (screen_height/2) - (100/2)
root.geometry('%dx%d+%d+%d' % (100, 100, x, y))
root.update()

def place_middle_of_screen():
    print("place_middle_of_screen")
    x = (screen_width/2) - (100/2)
    y = (screen_height/2) - (100/2)
    #root.geometry('%dx%d+%d+%d' % (100, 100, x, y))
    print(x, y)
    x = int(x)
    y = int(y)
    while True:
        if (root.winfo_x() != x, root.winfo_y() != y):
            print("Middle")
            # Float != Int
            print(root.winfo_x(), x)
            print(root.winfo_y(), y)
            if (root.winfo_x() >= x):
                print("Right 1")
                for i in range(int(root.winfo_x() - x)):
                    root.geometry("100x100" + "+" + str(root.winfo_x() - 1) + "+" + str(root.winfo_y()))
                    root.update()
            if (root.winfo_x() < x):
                print("Left 1")
                for i in range(int(root.winfo_x() - x) * -1):
                    root.geometry("100x100" + "+" + str(root.winfo_x() + 1) + "+" + str(root.winfo_y()))
                    root.update()
            if (root.winfo_y() >= y):
                print("Right 2")
                for i in range(int(root.winfo_y()) - int(y)):
                    root.geometry("100x100" + "+" + str(root.winfo_x()) + "+" + str(root.winfo_y() - 1))
                    root.update()
            #elif (root.winfo_x() < x, root.winfo_y() < y):
            if (root.winfo_y() < y):
                print("Left 2")
                for i in range(int(root.winfo_y()) - int(y)):
                    root.geometry("100x100" + "+" + str(root.winfo_x()) + "+" + str(root.winfo_y() + 1))
                    root.update()

        # Removing this statement below causes strange behaviour.
        if (root.winfo_x() == x, root.winfo_y() == y):
            break
        else:
            print(root.winfo_x(), root.winfo_y())
            break

def update_label():
    i = random.randrange(6)
    face_holder.set(str(random_faces[i]))
    root.update()

def update_pos():
    random_option = random.randrange(4)
    current_x, current_y = root.winfo_x(), root.winfo_y()
    print("Update_Pos", random_option)
    if (random_option == 0):
        current_x += 5
        current_y += 5
    elif (random_option == 1):
        current_x -= 5
        current_y -= 5
    elif (random_option == 2):
        current_x += 5
        current_y -= 5
    elif (random_option == 3):
        current_x -= 5
        current_y += 5
    print("x:", current_x, "y:", current_y)
    if (current_x <= 0):
        current_x = 1
    if (current_y <= 0):
        current_y = 1
    root.geometry("100x100" + "+" + str(current_x) + "+" + str(current_y))
    if (current_x >= screen_width):
        root.geometry("100x100" + "+" + str(-root.winfo_x()) + "+" + str(-root.winfo_x()))
    if (current_y >= screen_height or current_y <= 0):
        root.geometry("100x100" + "+" + str(-root.winfo_x()) + "+" + str(-root.winfo_x()))
    root.update()

def show_current_pos():
    print("Current_Cord")
    print("x", root.winfo_x())
    print("y", root.winfo_y())

def free_fall():
    while (root.winfo_y() <= 1000):
        print("Falling")
        root.geometry("100x100" + "+" + str(root.winfo_x()) + "+" + str(root.winfo_y() + 1))
        root.update()
    
x, y = 0, 0
def mouse_motion(event):
    global x, y
    show_current_pos()
    # Positive offset represent the mouse is moving to the lower right corner, negative moving to the upper left corner
    offset_x, offset_y = event.x - x, event.y - y  
    root.geometry('%dx%d+%d+%d' % (100, 100, root.winfo_x() + offset_x, root.winfo_y() + offset_y))

def mouse_press(event):
    global x, y
    update_label()
    x, y = event.x, event.y
    #root.after(2000)
    #root.after(1000, window_shake())

def window_shake():
    # May require threading.
    #oldtime = time.time()
    #print(time.time())
    #while True:
        #print(time.time())
        #if (time.time() - oldtime > 2):
    print("it's been a minute")
    for i in range(1000):
        update_pos()

def mouse_release(event):
    free_fall()
    place_middle_of_screen()

root.bind("<B1-Motion>", mouse_motion)
root.bind("<Button-1>", mouse_press)
root.bind("<ButtonRelease-1>", mouse_release)
root.bind('<Escape>', close)
update_label()

"""
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
"""
        
# Keep running window
root.mainloop()

# TODO: Window moves center of screen and changes center label.
# TODO: Reorganie code into classes.



