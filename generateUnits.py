#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from lxml import etree
from unidecode import unidecode
import os
import requests

# Constants
DIR = "dir"
FILE = "file"
GRADES = ["7", "8", "9", "10", "11", "12"]
LOCAL_BASE_URL = "."
REMOTE_BASE_URL = "http://juanxxiii.droppages.com/recursos/"
TEMPLATE_URL = "https://raw.githubusercontent.com/alemacgo/edurecursos/master/templates/dynamic-template.html"
SHEET_URL = "https://docs.google.com/spreadsheets/d/1Lz-ctPcNuQH19JHDnbs7H7OoArj--zrHK7UJZAuXuSc/edit#gid=0"

def get_spreadsheet():
    json_key = json.load(open('edurecursos-8415b4ddb61f.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    gc = gspread.authorize(credentials)

    return gc.open_by_url(SHEET_URL)

def parse_worksheet(spreadsheet, worksheet_index):
    worksheet = spreadsheet.get_worksheet(worksheet_index)
    data = worksheet.get_all_values()[1:] # Skip the headers

    grade = etree.Element(DIR, name=GRADES[worksheet_index])
    subject = None
    row_index = 1
    for row in data:
        row_index += 1
        subject_name = row[0]
        if subject_name: # New subject
            subject = etree.SubElement(grade, DIR, name=resource_name(subject_name))
        unit_name = row[1]
        resources_spreadsheet_link = row[2]
        if unit_name and resources_spreadsheet_link:
            unit = etree.SubElement(subject, FILE, link=resources_spreadsheet_link,\
                            unit_name=unit_name, name=resource_name(unit_name) + ".html")
            worksheet.update_cell(row_index, 4, get_url(unit))
    return grade

def get_url(tree):
    path = []
    while tree != None:
        path.append(tree.get("name"))
        tree = tree.getparent()
    path.reverse()
    return REMOTE_BASE_URL + "/".join(path)

def resource_name(text):
    text = text.strip().replace('  ', ' ').replace(' ', '-').lower()
    if type(text) == unicode:
        return unidecode(text)
    else:
        return text

def print_tree(root):
    print etree.tostring(root, pretty_print=True)

def get_tree(spreadsheet):
    root = etree.Element(DIR, name="recursos")
    for index, _ in enumerate(spreadsheet.worksheets()):
        root.append(parse_worksheet(spreadsheet, index))
    return root

def make_files(tree, path, html_template):
    if tree.tag == DIR:
        try:
            os.makedirs("/".join(path + [tree.get('name')]))
        except:
            pass
        for node in tree.iterchildren():
            make_files(node, path + [tree.get('name')], html_template)
    elif tree.tag == FILE:
        make_html(tree.get('unit_name'), tree.get('link'), \
                  "/".join(path + [tree.get('name')]), html_template)

def make_html(name, link, path, html_template):
    html = html_template.replace('*', name.encode('utf-8'), 1).replace('*', link, 1)
    fd = open(path, 'w')
    fd.write(html)
    fd.close()

def clean_directory(path):
    command = "rm -rf " + path + "/recursos"
    #print command
    os.system(command)

def main():
    spreadsheet = get_spreadsheet()
    tree = get_tree(spreadsheet)
    #tree = etree.fromstring(xml)
    html_template = requests.get(TEMPLATE_URL).text.encode('utf-8').strip()
    clean_directory(LOCAL_BASE_URL)
    make_files(tree, [LOCAL_BASE_URL], html_template)

if __name__ == "__main__":
    main()
