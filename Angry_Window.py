from tkinter import *
import time
import random
import sys
import time

random_faces = ["＼(^o^)／", "¯\_(ツ)_/¯", "\ (•◡•) /", "~(˘▾˘~)", "ヽ(•‿•)ノ", "(ﾉ^_^)ﾉ"]
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

current_cord_button = Button(root, text="Current_Cord", command=current_pos)
current_cord_button.pack()
"""

def place_middle_of_screen():
    x = (screen_width/2) - (100/2)
    y = (screen_height/2) - (100/2)
    root.geometry('%dx%d+%d+%d' % (100, 100, x, y))

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

def current_pos():
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
    current_pos()
    # Positive offset represent the mouse is moving to the lower right corner, negative moving to the upper left corner
    offset_x, offset_y = event.x - x, event.y - y  
    root.geometry('%dx%d+%d+%d' % (100, 100, root.winfo_x() + offset_x, root.winfo_y() + offset_y))

def mouse_press(event):
    global x, y
    update_label()
    x, y = event.x, event.y
    oldtime = time.time()
    print(time.time())
    while (x == event.x and y == event.y):
        if (time.time() - oldtime > 2):
            print("it's been a minute")
            for i in range(1000):
                update_pos()
            break

def mouse_release(event):
    free_fall()

root.bind("<B1-Motion>", mouse_motion)
root.bind("<Button-1>", mouse_press)
root.bind("<ButtonRelease-1>", mouse_release)
update_label()
place_middle_of_screen()
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
