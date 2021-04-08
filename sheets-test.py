import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from General import Constants


def main():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(Constants.api_json_path, scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    sheet = client.open('CS110 Recitation Role Sheet')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    print(sheet_instance)


if __name__ == '__main__':
    main()
