# google_sheets.py
import pandas as pd
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Scopes, Google Sheet ID, and range
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SHEET_ID = '18CMxp7QzHvYmwbFb3gWDJwL9o7Bxb0OJ_Us3YgIlvqs'
RANGE = 'lifting!A:N'

def get_sheet_data():
    creds = None
    if os.path.exists('api_files/token.json'):
        creds = Credentials.from_authorized_user_file('api_files/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('api_files/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('api_files/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return pd.DataFrame()  # Return an empty DataFrame if no data found
    else:
        # Ensure each row has the same number of columns
        max_columns = len(values[0])
        for i in range(1, len(values)):
            while len(values[i]) < max_columns:
                values[i].append('')  # Fill missing values with empty strings

        df = pd.DataFrame(values[1:], columns=values[0])  # Use the first row as column names
        df.dropna(inplace=True)  # Drop rows with None values
        return df

def main():
    df = get_sheet_data()
    return df

if __name__ == '__main__':
    dataframe = main()
    display(dataframe)  # Display the dataframe in the Jupyter notebook