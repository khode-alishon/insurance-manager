from tkinter import *
import tkinterDnD as tkdnd
from tkinter import ttk
import sys
sys.path.insert(0,r"classes\modules")
from tarafe import get_tarafe
import main

class App():

    def __init__(self, window = None):

        self.app_frame = Frame(window)

        self.search_argument = StringVar(self.app_frame)

        def farsi(what):
            return str(what).replace("ي", "ی").replace("ك", "ک")

        def search(*args):
            if len(self.search_argument.get()) < 3:
                pass
            else:
                if get_tarafe(farsi(str(self.search_argument.get())))[0] == "None":
                    mylbl.get("None")
                else:
                    mylbl.set(get_tarafe(farsi(self.search_argument.get()))[1][0])

        self.search_argument.trace('w', search)

        inp = Entry(self.app_frame, textvariable= self.search_argument)
        inp.pack()

        mylbl = StringVar(self.app_frame)
        label = Label(self.app_frame, textvariable=mylbl, bg = main.root_bg)
        label.pack()





    def run(self): 
        self.app_frame.grid(row = 0, column = 0)


