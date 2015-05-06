#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
#Tk, Frame, Label, Text, Button, BOTH, RIGHT, RAISED, W, N, E, S

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.parent.title("Crear unidad...")
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Enlace a la hoja de cálculo").grid(row=0, sticky=W)
        Label(self, text="Nombre de la unidad").grid(row=1, sticky=W)
        e1 = Entry(self, width=70)
        e1.insert(0, "https://docs.google.com/spreadsheets/...")
        e2 = Entry(self, width=70)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        abtn = Button(self, text="Crear", command=self.quit)
        abtn.grid(row=2, column=1, sticky=E)

   # def initUI(self):
   #     self.parent.title("Crear unidad...")
   #     self.style = Style()
   #     self.style.theme_use("default")

   #     frame = Frame(self, relief=RAISED, borderwidth=1)
   #     frame.pack(fill=BOTH, expand=1)

   #     self.pack(fill=BOTH, expand=1)

   #     closeButton = Button(self, text="Crear", command=self.quit)
   #     closeButton.pack(side=RIGHT, padx=5, pady=5)

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
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
