from tkinter import *
import tkinterDnD as tkdnd
from tkinter import ttk
import sys


class App():

    def __init__(self, window = None):

        self.app_frame = Frame(window)
        self.test_label = Label(self.app_frame, text = "File Validator")
        self.test_label.grid(row = 0, column = 0)
    
        

    def run(self): 
        self.app_frame.grid(row = 0, column = 0)

