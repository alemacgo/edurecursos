#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import os

# For the future, get the template from this URL instead of having it hardcoded
# Use BeautifulSoup to edit HTML nodes
# import requests
# TemplateURL = "https://raw.githubusercontent.com/alemacgo/edurecursos/master/templates/dynamic-template.html"
# page = requests.get(TemplateURL)
template = """
<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang=""> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="stylesheet" href="../css/bootstrap.min.css">
        <link rel="stylesheet" href="../css/styles.css">

        <link href='http://fonts.googleapis.com/css?family=Lato:400,900' rel='stylesheet' type='text/css'>

        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="../js/vendor/jquery-1.11.2.min.js"><\/script>')</script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-sheetrock/1.0.0/dist/sheetrock.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/1.1.2/handlebars.min.js"></script>
        <style>
            body { background-color: #E6E7FF; }
        </style>

    </head>
    <body>
        <!--[if lt IE 8]>
            <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        <div class="unit-name">
            <h1 id="unit-name">*</h1>
        </div>
        <div class="resource-list" id="hr">
            <script id="hr-template" type="text/x-handlebars-template">
            <a href="{{cells.Link}}" target="_blank">
                    <div class="resource">
                        <div class="row">
                            <span class="resource-number">{{{link num}}}</span>
                            <img class="resource-type" src="../img/{{cells.Tipo}}.png" />
                            <span class="resource-name">{{cells.Nombre}}</span>
                        </div>
                    </div>
            </a>
            </script>
        </div>

        <script id="spreadsheet-url">
            var spreadsheetUrl = "*";
        </script>
        <script src="../js/get-contents.js"></script>
        <script src="../js/main.js"></script>

        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <script>
            (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
            function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
            e=o.createElement(i);r=o.getElementsByTagName(i)[0];
            e.src='//www.google-analytics.com/analytics.js';
            r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
            ga('create','UA-XXXXX-X','auto');ga('send','pageview');
        </script>
    </body>
</html>
"""

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

def filename(string):
    # unidecode doesn't play well with Tkinter Entry's get()
    return string.strip().replace('  ', ' ').replace(' ', '-').lower() + ".html"

def createUnit():
    global template
    url = spreadsheetURLEntry.get()
    name = unitNameEntry.get()
    if url != DefaultURL and len(url) >= len(URLPrefix) and name != "":
        html = template.replace('*', name, 1).replace('*', url, 1)
        fd = open(filename(name), 'w')
        fd.write(html)
        fd.close()
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

master.mainloop()
