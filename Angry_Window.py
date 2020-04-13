from tkinter import *
import time
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
    index = 0
    while True:
        print(index)
        index += 1
        root.geometry("100x100" + "+" + str(index) + "+" + str(index))
        root.update()
        x = (screen_width/2) - (100/2)
        y = (screen_height/2) - (100/2)
        print(x, y)
        if (x == screen_width):
            root.geometry('%dx%d+%d+%d' % (100, 100, 0, 0))
        if (y == screen_height):
            root.geometry('%dx%d+%d+%d' % (100, 100, 0, 0))

face = Label(root, textvariable=variable)
face.place(x=25, y=25, anchor="center") 
face.pack()
start_button = Button(root, text="start", command=update_label)
start_button.pack()

start_button2 = Button(root, text="Start", command=update_pos)
start_button2.pack()

# Keep running window
root.mainloop()



