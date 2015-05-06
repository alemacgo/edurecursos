#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *

# MARK: Fetching the template and injecting the content

# MARK: Generating the .html file

# MARK: UI
DefaultURL = "https://docs.google.com/spreadsheets/..."
URLPrefix = "https://docs.google.com/spreadsheet"

def centerWindow(view):
    width = 680
    height = 100
    sh = view.winfo_screenheight()
    x = (view.winfo_screenwidth() - width)/2
    y = (view.winfo_screenheight() - height)/2
    view.geometry('%dx%d+%d+%d' % (width, height, x, y))

def clearText(event):
    spreadsheetURLEntry.config(fg="black")
    spreadsheetURLEntry.delete(0, END)

def createUnit():
    url = spreadsheetURLEntry.get()
    name = unitNameEntry.get()
    if url != DefaultURL and len(url) >= len(URLPrefix) and name != "":
        print url, name
        master.quit()

master = Tk()
centerWindow(master)
master.title("Crear unidad...")

Label(master, text="Enlace a la hoja de cálculo").grid(row=0, sticky=W)
spreadsheetURLEntry = Entry(master, width=70, fg="gray")
spreadsheetURLEntry.insert(0, DefaultURL)
spreadsheetURLEntry.grid(row=0, column=1)

spreadsheetURLEntry.bind('<Button-1>', clearText)

Label(master, text="Nombre de la unidad").grid(row=1, sticky=W)
unitNameEntry = Entry(master, width=70)
unitNameEntry.grid(row=1, column=1)

createButton = Button(master, text="Crear", command=createUnit)
createButton.grid(row=2, column=1, sticky=E)

#master.mainloop()
