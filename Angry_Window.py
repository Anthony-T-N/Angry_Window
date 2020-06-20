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
# TODO: Determine why duplicated windows not updating labels.

from tkinter import *
import random
import sys
import threading
import time

class Angry_Window():

    # ~ Constructor
    def __init__(self):
        self.random_faces = ["＼(^o^)／", "¯\_(ツ)_/¯", "\ (•◡•) /", "~(˘▾˘~)", "ヽ(•‿•)ノ", "(ﾉ^_^)ﾉ", "ʕっ•ᴥ•ʔっ"]
        # Blank window.
        self.root = Tk()
        self.root.title("Angry_Window")
        self.root.geometry("100x100")
        self.root.configure(bg="#0e4f73")
        self.root.config(cursor='heart')
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

        # Place middle of screen.
        self.root.screen_width = self.root.winfo_screenwidth()
        self.root.screen_height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (100, 100, ((self.root.screen_width/2) - (100/2)), ((self.root.screen_height/2) - (100/2))))
        self.root.update()

        # Root binding.
        self.root.bind("<B1-Motion>", self.mouse_motion)
        self.root.bind("<Button-1>", self.mouse_press)
        self.root.bind("<ButtonRelease-1>", self.mouse_release)
        self.root.bind('<Escape>', self.close)
        self.root.bind('<Shift_L>', self.self_control)
        self.root.bind('<Control_L>', self.follow_mouse)
        self.root.bind('<Control_R>', self.window_movement)
        self.root.bind("<space>", self.window_bounce)
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
        print("Update_label")
        self.face_holder.set(str(self.random_faces[random.randrange(6)]))
        self.root.update()

    def pos_spasm(self):
        random_option = random.randrange(4)
        current_x, current_y = self.root.winfo_x(), self.root.winfo_y()
        print("pos_spasm", random_option)
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

        self.root.geometry("100x100" + "+" + str(current_x) + "+" + str(current_y))
        if (self.root.winfo_x() <= 0):
            print(self.root.winfo_x(), "<=", self.root.screen_width, "Refocus back on x")
            self.root.geometry("100x100" + "+" + str(self.root.winfo_x() + 5) + "+" + str(self.root.winfo_y()))
            self.root.update()
        if (self.root.winfo_x() >= self.root.screen_width):
            print(self.root.winfo_x(), ">=", self.root.screen_width, "Refocus back on x")
            self.root.geometry("100x100" + "+" + str(self.root.winfo_x() - 5) + "+" + str(self.root.winfo_y()))
            self.root.update()
        if (self.root.winfo_y() <= 0):
            print(self.root.winfo_y(), ">=", "0", "Refocus back on y")
            self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() + 5))
            self.root.update()
        if (self.root.winfo_y() >= self.root.screen_height):
            print(self.root.winfo_y(), ">=", self.root.screen_height, "Refocus back on y")
            self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() - 5))
            self.root.update()
        self.root.update()

    def show_current_pos(self):
        print("Current_Coordinates")
        print("x", self.root.winfo_x())
        print("y", self.root.winfo_y())

    def free_fall(self):
        # Value hard-coded. Make dynamic based on screen window dimension.
        while (self.root.winfo_y() <= (self.root.winfo_screenheight() - 100)):
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
        self.window_colour_change()
        self.update_label()
        self.root.x, self.root.y = event.x, event.y

    def window_shake(self):
        for _ in range(1000):
            self.pos_spasm()

    def mouse_release(self, event):
        self.free_fall()

    def window_colour_change(self):
        for _ in range(10):
            internal_option = random.randrange(4)
            colour_list = ["0e4f73", "DBDE31", "266D15", "D21F37"]
            print("#" + colour_list[internal_option])
            self.root.configure(bg="#" + colour_list[internal_option])
            self.root.update()
        self.root.after(50000, self.window_colour_change)
            #time.sleep(0.1)

    def follow_mouse(self, event):
        while True:
            current_mouse_x = self.root.winfo_pointerx()
            current_mouse_y = self.root.winfo_pointery()
            
            print("x:", current_mouse_x, "y:", current_mouse_y, "x:", self.root.winfo_x(), "y:", self.root.winfo_y())
            print("x:", current_mouse_x, "y:", current_mouse_y, "x:", self.root.winfo_rootx(), "y:", self.root.winfo_rooty())

            # Negative offset for cursor to reach middle of window.
            if (self.root.winfo_x() > self.root.winfo_pointerx() - 50):
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() - 1) + "+" + str(self.root.winfo_y()))
                self.root.update()
            
            if (self.root.winfo_x() < self.root.winfo_pointerx() - 50):
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() + 1) + "+" + str(self.root.winfo_y()))
                self.root.update()
            
            if (self.root.winfo_y() > self.root.winfo_pointery() - 50):
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() - 1))
                self.root.update()
            
            if (self.root.winfo_y() < self.root.winfo_pointery() - 50):
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() + 1))
                self.root.update()

    def window_movement(self, event):
        print("Function: window_movement")
        while True:
            internal_option = random.randrange(4)
            print("Internal_Option:", internal_option)
            print("x:", self.root.winfo_x(), "y:", self.root.winfo_y())
            print("x:", self.root.winfo_rootx(), "y:", self.root.winfo_rooty())
            self.update_label()
            if (internal_option == 0):
                print("->")
                for _ in range(10):
                    self.root.geometry("100x100" + "+" + str(self.root.winfo_x() + 10) + "+" + str(self.root.winfo_y()))
                    self.root.update()
                time.sleep(1)
            if (internal_option == 1):
                print("<-")
                for _ in range(10):
                    self.root.geometry("100x100" + "+" + str(self.root.winfo_x() - 10) + "+" + str(self.root.winfo_y()))
                    self.root.update()
                time.sleep(1)
            if (internal_option == 2):
                print("^")
                for _ in range(10):
                    self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() - 10))
                    self.root.update()
                time.sleep(1)
            if (internal_option == 3):
                print("!")
                for _ in range(10):
                    self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() + 10))
                    self.root.update()
                time.sleep(1)
            self.root.update()
            
            if (self.root.winfo_x() <= 0):
                print(self.root.winfo_x(), "<=", self.root.screen_width, "Refocus back on x")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() + 5) + "+" + str(self.root.winfo_y()))
                self.root.update()
            if (self.root.winfo_x() >= self.root.screen_width):
                print(self.root.winfo_x(), ">=", self.root.screen_width, "Refocus back on x")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() - 5) + "+" + str(self.root.winfo_y()))
                self.root.update()
            if (self.root.winfo_y() <= 0):
                print(self.root.winfo_y(), ">=", "0", "Refocus back on y")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() + 5))
                self.root.update()
            if (self.root.winfo_y() >= self.root.screen_height):
                print(self.root.winfo_y(), ">=", self.root.screen_height, "Refocus back on y")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x()) + "+" + str(self.root.winfo_y() - 5))
                self.root.update()
            self.root.update()

    
    def window_bounce(self, event):
        # Very messy function.
        top_edge_switch = False
        right_edge_switch = False
        left_edge_switch = False
        bottom_edge_switch = False

        while True:
            print("x:", self.root.winfo_rootx(), "y:", self.root.winfo_rooty())
            if (self.root.winfo_x() >= 1820 or top_edge_switch == True):
                print("Right-Edge")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() - 1) + "+" + str(self.root.winfo_y() - 1))
                self.root.update()
                top_edge_switch = True
                right_edge_switch = False

                left_edge_switch = False
                bottom_edge_switch = False

            if (self.root.winfo_y() <= 1 or left_edge_switch == True):
                print(right_edge_switch)
                print("Top-Edge")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() - 1) + "+" + str(self.root.winfo_y() + 1))
                self.root.update()
                left_edge_switch = True
                top_edge_switch = False

                right_edge_switch = False
                bottom_edge_switch = False
                
            if (self.root.winfo_x() <= 0 or bottom_edge_switch == True):
                print("Left-Edge")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() + 1) + "+" + str(self.root.winfo_y() + 1))
                self.root.update()
                bottom_edge_switch = True
                left_edge_switch = False

                top_edge_switch = False
                right_edge_switch = False
                
            if (self.root.winfo_y() >= 980 or right_edge_switch == True):
                print("Bottom-Edge")
                self.root.geometry("100x100" + "+" + str(self.root.winfo_x() + 1) + "+" + str(self.root.winfo_y() - 1))
                self.root.update()
                right_edge_switch = True
                bottom_edge_switch = False

                bottom_edge_switch = False
                left_edge_switch = False
                

    def self_control(self, event):
        while True:
            internal_option = random.randrange(5)
            print("Internal_Option:", internal_option)
            if (internal_option == 0):
                self.pos_spasm()
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
    Angry_Window()
    """
    list_of_windows = []
    for _ in range(4):
        current_thread = threading.Thread(target=Angry_Window)
        current_thread.start()
        list_of_windows.append(current_thread)
    """

if __name__ == "__main__":
    main()







