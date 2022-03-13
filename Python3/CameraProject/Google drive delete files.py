#!/usr/bin/python
from __future__ import print_function
import os.path
from datetime import datetime,timedelta
from datetime import date
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8001)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    DRIVE = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    #results = DRIVE.files().list( pageSize=10, fields="nextPageToken, files(id, name, createdTime)").execute()

    items = DRIVE.files().list(fields="nextPageToken, files(id, name, createdTime)").execute().get('files', [])

    today = date.today()
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            #print(u'{0} ({1})'.format(item['name'], item['createdTime']))
            print(item)
            #checking if the file age is older then 5 days
            fileAgeinDays = (datetime.utcnow() - datetime.strptime(item['createdTime'], '%Y-%m-%dT%H:%M:%S.%fZ')).days
            if fileAgeinDays > 5:
                DRIVE.files().delete(item['id']).execute()



if __name__ == '__main__':
    main()
~
