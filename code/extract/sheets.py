# This code fetches data from RSS Store on Google Sheet

from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
from decouple import config


def sheets(): # Get a List of RSS feed from Google Sheets
    # Set environment variables
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'keys.json'

    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    CREDS = None
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID and range of a sample spreadsheet.
    SPREADSHEET_ID = config('SPREADSHEET_ID')
    SPREADSHEET_RANGE = 'feed!C2:C113'
    service = build('sheets', 'v4', credentials=CREDS)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=SPREADSHEET_RANGE).execute()
    values = result.get('values', [])  # List of List
    return values


def singleList(list):      #  Make a List out of List of Lists
    RSS = []
    for sublist in list:
        for item in sublist:
            RSS.append(item)
    return RSS


def main(): 
    list = sheets()
    RSS = singleList(list)
    return RSS


if __name__ == "__sheets__":  # Dunder to run the code as a module and not script
   main()
