import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# initiates OAuth 2.0 process & returns credentials
def authenticate():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=8080)
        # save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


# returns user's calendar
def get_calendar(credentials):
    return build('calendar', 'v3', credentials=credentials)

###################################################################################################


# might consider:
# description (string)
# colorId (string)
# location (string)
# EVENT = {
#     'summary': 'lol', # ,<- title
#     'description': 'lolol',
#     'location': '10332 Adobe Cir, Irvine, CA',
#     'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
#     'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
# }