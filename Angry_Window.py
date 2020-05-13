""" ---

    File name: Angry_Window.py
    Date created: 04/04/2020
    Functional Version Finished: 04/05/2020

"""

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

__author__ = 'Anthony T Nguyen'
__version__ = '1.0.0'
__date__ = ''
__status__ = 'Development'

# TODO: Clean up.
# TODO: Simplify some functions.

from tkinter import *
import time
import random
import sys
import threading

class Angry_Window():

    # ~ Constructor
    def __init__(self):
        self.random_faces = ["＼(^o^)／", "¯\_(ツ)_/¯", "\ (•◡•) /", "~(˘▾˘~)", "ヽ(•‿•)ノ", "(ﾉ^_^)ﾉ", "ʕっ•ᴥ•ʔっ"]
        # Blank window.
        self.root = Tk()
        self.root.title("Angry_Window")
        self.root.geometry("100x100")
        self.root.configure(bg="#0e4f73")
        self.root.config(highlightbackground="white", highlightcolor="white", highlightthickness=3)
        self.root.overrideredirect(True)

        self.root.x = 0
        self.root.y = 0

        # Fixed window dimensions. Disables maximise button.
        self.root.resizable(width=False, height=False)
        self.root.lift()
        self.root.attributes("-topmost", True)

        self.face_holder = StringVar()
        face = Label(self.root, textvariable=self.face_holder, font='TkDefaultFont 12 bold')
        face.place(relx=.5, rely=.5, anchor="center")

        self.root.screen_width = self.root.winfo_screenwidth()
        self.root.screen_height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (100, 100, ((self.root.screen_width/2) - (100/2)), ((self.root.screen_height/2) - (100/2))))
        self.root.update()

        self.root.bind("<B1-Motion>", self.mouse_motion)
        self.root.bind("<Button-1>", self.mouse_press)
        self.root.bind("<ButtonRelease-1>", self.mouse_release)
        self.root.bind('<Escape>', self.close)
        self.root.bind('<Shift_L>', self.self_control)
        self.root.after(0, self.update_label())

        # Keep running window
        self.root.mainloop()

    def place_middle_of_screen(self):
        print("place_middle_of_screen")
        x = int((self.root.screen_width/2) - (100/2))
        y = int((self.root.screen_height/2) - (100/2))
        while True:
            if (self.root.winfo_x() != x, self.root.winfo_y() != y):
                print(self.root.winfo_x(), x)
                print(self.root.winfo_y(), y)
                if (self.root.winfo_x() >= x):
                    print("Right 1")
                    for _ in range(int(self.root.winfo_x() - x)):
                        self.root.geometry("100x100" + "+" + str(self.root.winfo_x() - 1) + "+" + str(self.root.winfo_y()))
                        self.root.update()
                if (self.root.winfo_x() < x):
                    print("Left 1")
                    for _ in range(int(self.root.winfo_x() - x) * -1):
                        self.root.geometry("100x100" + "+" + str(self.root.winfo_x() + 1) + "+" + str(self.root.winfo_y()))
                        self.root.update()
                if (self.root.winfo_y() >= y):
                    print("Right 2")
                    for _ in range(int(self.root.winfo_y()) - int(y)):
                        self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() - 1))
                        self.root.update()
                #elif (self.root.winfo_x() < x, self.root.winfo_y() < y):
                if (self.root.winfo_y() < y):
                    print("Left 2")
                    for _ in range(int(self.root.winfo_y()) - int(y)):
                        self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() + 1))
                        self.root.update()

            # Removing this statement below causes strange behaviour.
            if (self.root.winfo_x() == x, self.root.winfo_y() == y):
                break
            else:
                print(self.root.winfo_x(), self.root.winfo_y())
                break

    def update_label(self):
        print("Hello")
        self.face_holder.set(str(self.random_faces[random.randrange(6)]))
        self.root.update()

    def update_pos(self):
        random_option = random.randrange(4)
        current_x, current_y = self.root.winfo_x(), self.root.winfo_y()
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
        self.root.geometry("100x100" + "+" + str(current_x) + "+" + str(current_y))
        if (current_x >= self.root.screen_width):
            self.root.geometry("100x100" + "+" + str(-self.root.winfo_x()) + "+" + str(-self.root.winfo_x()))
        if (current_y >= self.root.screen_height or current_y <= 0):
            self.root.geometry("100x100" + "+" + str(-self.root.winfo_x()) + "+" + str(-self.root.winfo_x()))
        self.root.update()

    def show_current_pos(self):
        print("Current_Cord")
        print("x", self.root.winfo_x())
        print("y", self.root.winfo_y())

    def free_fall(self):
        while (self.root.winfo_y() <= 1000):
            print("Falling...")
            self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() + 1))
            self.root.update()
        
    def mouse_motion(self, event):
        self.root.x, self.root.y
        self.show_current_pos()
        # Positive offset represent the mouse is moving to the lower right corner, negative moving to the upper left corner
        offset_x, offset_y = event.x - self.root.x, event.y - self.root.y  
        self.root.geometry('%dx%d+%d+%d' % (100, 100, self.root.winfo_x() + offset_x, self.root.winfo_y() + offset_y))

    def mouse_press(self, event):
        self.root.x, self.root.y
        print("Update_label")
        self.update_label()
        self.root.x, self.root.y = event.x, event.y
        #self.root.after(2000)
        #self.root.after(1000, window_shake())

    def window_shake(self):
        # May require threading.
        #oldtime = time.time()
        #print(time.time())
        #while True:
            #print(time.time())
            #if (time.time() - oldtime > 2):
        for _ in range(1000):
            self.update_pos()

    def mouse_release(self, event):
        self.free_fall()

    def self_control(self, event):
        while True:
            internal_option = random.randrange(5)
            print("Internal_Option:", internal_option)
            if (internal_option == 0):
                self.update_pos()
            elif (internal_option == 1):
                self.update_label()
            elif (internal_option == 2):
                self.free_fall()
            elif (internal_option == 3):
                self.window_shake()
            elif (internal_option == 4):
                self.place_middle_of_screen()

    def close(self, event):
        self.root.destroy()

def main():
    list_of_windows = []
    for _ in range(4):
        current_thread = threading.Thread(target=Angry_Window)
        current_thread.start()
        list_of_windows.append(current_thread)

if __name__ == "__main__":
    main()
