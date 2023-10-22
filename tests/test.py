import pandas as pd
import numpy as np
import xlsxwriter
from tkinter import *
import tkinterDnD
from tkinter import filedialog

root = Tk()

root.columnconfigure(1, weight = 4)
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.geometry("600x400")

testcnvs = Frame(root)
testcnvs.rowconfigure(0, weight=1)
testcnvs.columnconfigure(0, weight=1)
testcnvs.grid(sticky=NSEW, row = 0, column = 1, rowspan= 3)
testcnvs.config(bg = "black")
cnvs_lbl = Label(testcnvs, text = "اطلاعات", font="Arial 18 bold", bg = "black", fg = "white")
cnvs_lbl.grid(row = 0, column= 0, sticky=NSEW)
root.title("علیرضا رباطجزی - شماره بیمه نامه: 226")


est = Label(root, text = "استعلام").grid(sticky=NSEW, row = 0, column= 0)
vld = Label(root, text = "بررسی فایل").grid(sticky=NSEW, row = 1, column= 0)
gzrsh = Label(root, text = "گزارشات").grid(sticky=NSEW, row = 2, column= 0)




root.mainloop()