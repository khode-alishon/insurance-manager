import pandas as pd
import numpy as np
import xlsxwriter
from tkinter import *
import tkinterDnD


root = Tk()

root.columnconfigure(1, weight = 4)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.geometry("600x400")

a = ["1","2"]
print("2" in a)

root.mainloop()