#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import Tk, RIGHT, Frame, Button, BOTH, RAISED
from ttk import Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.parent.title("Crear unidad...")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        self.pack(fill=BOTH, expand=1)

        closeButton = Button(self, text="Crear", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        #okButton = Button(self, text="OK")
        #okButton.pack(side=RIGHT)

    def centerWindow(self):
        width = 700
        height = 150
        sh = self.parent.winfo_screenheight()
        x = (self.parent.winfo_screenwidth() - width)/2
        y = (self.parent.winfo_screenheight() - height)/2
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

def main():
    root = Tk()
    root.geometry("700x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
