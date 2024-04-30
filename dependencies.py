from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("PDT_App_Backend.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
google_sheet = file.open("Data Collection") #open sheet

sheet = google_sheet.worksheet('DATA') 

#data = ['4/29/2024', 'Test', None, 0, 'This was a test from the PDT App Backend']

#response = sheet.append_row(data, table_range = 'A1:E1', value_input_option = 'USER_ENTERED', include_values_in_response=True)

#print(response)