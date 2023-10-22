from tkinter import *
import tkinterDnD as tkdnd
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
import sys, PIL
sys.path.insert(0,r"classes\windows")
import validator, mohasebe, gozaresh,estelaam

root_bg = "#222222"
win_bg = "#353535" 
win_fg = "#ffffff"
btn_bg = "#595959"


def main():
    
    def button_hover(e, lbl):
        print(label["text"])

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


    khesarat_app_label = Label(apps_nav, text = "خسارت", bg = btn_bg, fg = win_fg, font = "Bnazanin 16 bold")
    khesarat_app_label.grid(row = 0, column=0, sticky= NSEW, padx=10, pady = 10)

    estelaam_app_label = Label(apps_nav, text = "استعلام", bg = btn_bg, fg = win_fg, font = "Bnazanin 16 bold")
    estelaam_app_label.grid(row = 1, column=0, sticky= NSEW, padx=10, pady = 10)

    tarafe_app_label = Label(apps_nav, text = "تعرفه", bg = btn_bg, fg = win_fg, font = "Bnazanin 16 bold")
    tarafe_app_label.grid(row = 2, column=0, sticky= NSEW, padx=10, pady = 10)

    file_app_label = Label(apps_nav, text = "بررسی فایل", bg = btn_bg, fg = win_fg, font = "Bnazanin 16 bold")
    file_app_label.grid(row = 3, column=0, sticky= NSEW, padx=10, pady = 10)

    report_app_label = Label(apps_nav, text = "گزارشات", bg = btn_bg, fg = win_fg, font = "Bnazanin 16 bold")
    report_app_label.grid(row = 4, column=0, sticky= NSEW, padx=10, pady = 10)

    main_nav_labels = [khesarat_app_label, estelaam_app_label, tarafe_app_label, file_app_label, report_app_label]

    for label in main_nav_labels:
        label.bind("<Enter>", lambda e: button_hover(e = e, lbl = label))


    root.mainloop()


if __name__ == "__main__":
    main()