import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('edurecursos-8415b4ddb61f.json'))
scope = ['https://spreadsheets.google.com/feeds']
sheet_url = 'https://docs.google.com/spreadsheets/d/1Lz-ctPcNuQH19JHDnbs7H7OoArj--zrHK7UJZAuXuSc/edit#gid=0'

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
gc = gspread.authorize(credentials)

wks = gc.open_by_url(sheet_url).sheet1
print wks
