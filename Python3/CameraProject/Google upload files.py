#!/usr/bin/python
from __future__ import print_function
import os.path
import glob
import os
from os import walk
from datetime import datetime,timedelta
from datetime import date
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
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
    files = glob.glob("/opt/pv01/ftp/**/*.mp4", recursive=True)    # the ** will tell globe to search the folder recursive
    for i in files:
        file_metadata = {'name': i.split('/')[7] }
        media  = MediaFileUpload(i, mimetype='video/mp4')
        uploadFile = DRIVE.files().create( body = file_metadata, media_body = media,fields='id').execute()
        print (uploadFile.get('id'))
        os.remove(i)
        print ("file"+i+"was removed")

if __name__ == '__main__':
    main()
