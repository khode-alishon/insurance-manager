from tkinter import *
import tkinterDnD as tkdnd
from tkinter import ttk
import sys
sys.path.insert(0,r"classes\modules")
import tarafe

def main():
    root = tkdnd.Tk()
    root.title("estelaam")
    search_argument = StringVar(root)

    def farsi(what):
        return what.replace("ي", "ی").replace("ك", "ک")

    def search(*args):
        if len(search_argument.get()) < 3:
            pass
        else:
            mylbl.set(tarafe.tarafe_get(search_argument = farsi(str(search_argument.get())))[0][0] )
            return tarafe.tarafe_get(search_argument = farsi(str(search_argument.get())))

    search_argument.trace('w', search)

    inp = Entry(root, textvariable= search_argument)
    inp.pack()

    mylbl = StringVar(root)
    label = Label(root, textvariable=mylbl)
    label.pack()

    root.mainloop()



if __name__ == "__main__":
    main()