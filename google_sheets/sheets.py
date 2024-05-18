from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("PDT_App_Backend.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread

# Initialize the Google Sheets
data_collection = file.open("Data Collection") 
requests_from_friends = file.open("PDT Requests from Friends")

data_collection_DATA = data_collection.worksheet('DATA') 
requests_from_friends_REQUESTS = requests_from_friends.worksheet('Requests')