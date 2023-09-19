from tkinter import *
import tkinterDnD as tkdnd
from tkinter import ttk
import sys
sys.path.insert(0,r"classes\windows")
import validator, mohasebe, gozaresh,estelaam


mains = [
    validator.main,
    mohasebe.main,
    gozaresh.main,
    estelaam.main
]

def main():
    
    root = tkdnd.Tk()

    def do(what):
        what()

    val = Button(text = "val", command= validator.main)
    val.pack()

    mohaseb = Button(text = "mohaseb", command= mohasebe.main)
    mohaseb.pack()

    gozar = Button(text = "gozar", command= gozaresh.main)
    gozar.pack()

    est = Button(text = "est", command= estelaam.main)
    est.pack()


    root.mainloop()


if __name__ == "__main__":
    main()