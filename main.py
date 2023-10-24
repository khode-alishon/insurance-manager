from tkinter import *
import tkinterDnD as tkdnd
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
import sys, PIL
sys.path.insert(0,r"classes\windows")
import validator, mohasebe, gozaresh,estelaam, tarafe_window

root_bg = "#222222"
win_bg = "#353535" 
win_fg = "#ffffff"
btn_bg = "#595959"

class MainNavButton(Label):
    def __init__(self, master,row = 0, column = 0, app = None, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.config(bg = btn_bg, fg = win_fg, font = "Bnazanin 16 bold")
        self.grid(row = row, column= column, sticky= NSEW, padx=10, pady = 10)
        self.bind("<Enter>", self.onhover)
        self.bind("<Button-1>", self.run)

    def onhover(self, e):
        pass



    def run(self, e):
        global app_window
        self.tst = self.app.App(window = app_window)
        try:
            for child in app_window.winfo_children():
                child.grid_forget()
        except:
            pass

        self.tst.run()

def main():
    global app_window

    def button_hover(e, lbl):
        print(lbl["text"])

    root = Tk()
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.columnconfigure(1, weight=5)
    root.columnconfigure(0, weight=1)
    root.config(bg = root_bg)
    root.geometry("720x480")



    apps_nav = Frame(root, bg = win_bg)
    apps_nav.grid(row = 0, column = 0, sticky=NSEW, rowspan=5, padx=20, pady = 20)
    apps_nav.columnconfigure(0, weight=1)
    apps_nav.rowconfigure(0, weight=1)
    apps_nav.rowconfigure(1, weight=1)
    apps_nav.rowconfigure(2, weight=1)
    apps_nav.rowconfigure(3, weight=1)
    apps_nav.rowconfigure(4, weight=1)

    app_window = Frame(root, bg = win_bg)
    app_window.grid(row = 0, column=1, sticky=NSEW, rowspan=5, padx=10, pady = 20)


    khesarat_app_label = MainNavButton(apps_nav, text = "خسارت", row = 0, column=0, app = mohasebe)
    estelaam_app_label = MainNavButton(apps_nav, text = "استعلام", row = 1, column=0, app = estelaam)
    tarafe_app_label = MainNavButton(apps_nav, text = "تعرفه", row = 2, column=0, app = tarafe_window)
    file_app_label = MainNavButton(apps_nav, text = "بررسی فایل", row = 3, column=0, app = validator)
    report_app_label = MainNavButton(apps_nav, text = "گزارشات", row = 4, column=0, app = gozaresh)


    root.mainloop()


if __name__ == "__main__":
    main()