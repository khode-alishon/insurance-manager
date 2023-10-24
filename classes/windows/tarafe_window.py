from tkinter import *
import tkinterDnD as tkdnd
from tkinter import ttk
import sys
sys.path.insert(0,r"classes\modules")
from tarafe import get_tarafe


class TarafeLabel(Label):
    def __init__(self, master, **kwargs):
        super.__init__(self, master, kwargs)


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
                    print("not found")
                else:
                    #mylbl.set(get_tarafe(farsi(self.search_argument.get()))[1][0])
                    found = get_tarafe(farsi(self.search_argument.get()))
                    for i in found:
                        print(i[0]) 

        self.search_argument.trace('w', search)

        inp = Entry(self.app_frame, textvariable= self.search_argument)
        inp.pack()

        





    def run(self): 
        self.app_frame.grid(row = 0, column = 0)


