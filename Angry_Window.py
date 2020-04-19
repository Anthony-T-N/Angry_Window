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
    #time.sleep(1)
    if (i >= 4):
        i = 0
    variable.set(str(random_text[i]))
    i += 1
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

def update_rand_pos():
    random_x_cord = random.randrange(1920)
    random_y_cord = random.randrange(1080)
    root.geometry("100x100" + "+" + str(random_x_cord) + "+" + str(random_y_cord))
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
        print("x", current_x1)
        print("y", current_y2)
    else:
        pass

start_button2 = Button(root, text="Start", command=update_pos)
start_button2.pack()

current_cord_button = Button(root, text="Current_Cord", command=current_pos)
current_cord_button.pack()

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
        time.sleep(0.1)
        update_label()

# Keep running window
root.mainloop()

