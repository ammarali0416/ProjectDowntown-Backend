import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Path to your service account key file
KEY_FILE_LOCATION = 'PDT_App_Backend.json'

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Authenticate using the service account key file
credentials = service_account.Credentials.from_service_account_file(KEY_FILE_LOCATION, scopes=SCOPES)

# Build the Drive API client
service = build('drive', 'v3', credentials=credentials)