#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import os
import requests

# Future:
# Use BeautifulSoup to edit HTML nodes

TemplateURL = "https://raw.githubusercontent.com/alemacgo/edurecursos/master/templates/dynamic-template.html"

# MARK: UI
PlaceholderSpreadsheetURL = "https://docs.google.com/spreadsheets/..."
URLPrefix = "https://docs.google.com/spreadsheet"
WebsiteBaseURL = "http://juanxxiii.droppages.com/unidades/"

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

def filename(string):
    # unidecode doesn't play well with Tkinter Entry's get()
    return string.strip().replace('  ', ' ').replace(' ', '-').lower() + ".html"

def createUnit(r, *args, **kwargs):
    url = spreadsheetURLEntry.get()
    name = unitNameEntry.get()
    if url != PlaceholderSpreadsheetURL and len(url) >= len(URLPrefix) and name != "":
        html = r.text.encode('utf-8').strip()
        html = html.replace('*', name, 1).replace('*', url, 1)
        fileName = filename(name)
        fd = open(fileName, 'w')
        fd.write(html)
        fd.close()
        popup = Toplevel()
        centerWindow(popup)
        Label(popup, text="La unidad fue creada. Enlace: ", height=0, width=100).pack()
        createSelectableText(popup, WebsiteBaseURL + fileName).pack()
        Button(popup, text="Salir", command=master.quit).pack()

def createSelectableText(context, text):
    w = Text(context, height=1, borderwidth=0)
    w.insert(1.0, text)
    w.configure(inactiveselectbackground=w.cget("selectbackground"))
    return w

def fetchTemplate(event = None):
    requests.get(TemplateURL, hooks=dict(response=createUnit))

master = Tk()
centerWindow(master)
master.title("Crear unidad...")

Label(master, text="Enlace a la hoja de cálculo").grid(row=0, sticky=W)
spreadsheetURLEntry = Entry(master, width=70, fg="gray")
spreadsheetURLEntry.insert(0, PlaceholderSpreadsheetURL)
spreadsheetURLEntry.grid(row=0, column=1)

spreadsheetURLEntry.bind('<Button-1>', clearText)

Label(master, text="Nombre de la unidad").grid(row=1, sticky=W)
unitNameEntry = Entry(master, width=70)
unitNameEntry.grid(row=1, column=1)

createButton = Button(master, text="Crear", command=fetchTemplate)
createButton.grid(row=2, column=1, sticky=E)

master.bind('<Return>', createUnit)

master.mainloop()
