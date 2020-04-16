from tkinter import *
import time
import random
# Blank window.
root = Tk()
root.title("Evil_Window")
root.geometry("100x100")
root.configure(bg="black")
#root.overrideredirect(True)
# Cannot change dimensions of window. Disables maxmise button
#root.resizable(width=False, height=False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width)
print(screen_height)

topFrame = Frame(root)
topFrame.pack()

x = (screen_width/2) - (100/2)
y = (screen_height/2) - (100/2)
root.geometry('%dx%d+%d+%d' % (100, 100, x, y))

#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)

#welcome_text = Label(topFrame, text="Welcome")
#welcome_text.pack(side="bottom")

#contentplaceholder = Label(bottomFrame, text="Contentplaceholder")
#contentplaceholder.pack(side="bottom")

variable = StringVar()

random_text = ["＼(^o^)／", "¯\_(ツ)_/¯", "\ (•◡•) /", "~(˘▾˘~)", "ヽ(•‿•)ノ", "(ﾉ^_^)ﾉ"]

def update_label():
    i = 0
    while 1:
        #time.sleep(1)
        if (i >= 4):
            i = 0
        variable.set(str(random_text[i]))
        i += 1
        root.update()

def update_pos():
    random_number = random.randrange(10)
    index = 0
    while True:
        if (index == 0 or index == 100):
            random_number = random.randrange(1000)
        random_switch = random.randrange(1)
        random_number += 1
        #time.sleep(0.01)
        print(index)
        index += 1
        root.geometry("100x100" + "+" + str(-random_number) + "+" + str(-random_number))
        if (random_switch == 0):
            root.geometry("100x100" + "+" + str(random_number) + "+" + str(random_number))
        if (random_switch == 1):
            root.geometry("100x100" + "+" + str(-random_number) + "+" + str(-random_number))
        current_x = root.winfo_x()
        current_y = root.winfo_y()
        print(current_x, current_y)
        if (current_x >= screen_width):
            random_number = random.randrange(1000)
        if (current_y >= screen_height):
            random_number = random.randrange(1000)
        root.update()

face = Label(root, textvariable=variable)
face.place(x=25, y=25, anchor="center")
face.pack()
start_button = Button(root, text="start", command=update_label)
start_button.pack()

def current_pos():
    current_x1 = root.winfo_x()
    current_y2 = root.winfo_y()
    if (current_x1 != root.winfo_x() or current_y2 != root.winfo_y):
        print("Current_Cord")
        print(current_x)
        print(current_y)
    else:
        pass
    current_x = root.winfo_x()
    current_y = root.winfo_y()

start_button2 = Button(root, text="Start", command=update_pos)
start_button2.pack()

current_cord_button = Button(root, text="Current_Cord", command=current_pos)
current_cord_button.pack()

current_pos()
# Keep running window
root.mainloop()


