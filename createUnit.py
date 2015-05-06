#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import Tk, Frame, BOTH

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.parent.title("Crear unidad...")
        self.pack(fill=BOTH, expand=1)

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
