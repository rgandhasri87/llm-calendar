import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


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
def getCalendar(credentials):
    return build('calendar', 'v3', credentials=credentials)


# creates event in calendar & returns event
def create_event_in_calendar(calendar, body, calendarId='primary', sendNotifications=True):
    try:
        event = calendar.events().insert(calendarId=calendarId, sendNotifications=sendNotifications, body=body).execute()
        print(f"successfully created event with body {body}")
        return event
    except Exception as e:
        print(f"failed to create event with body {body}. Error {e}")
        return False


###################################################################################################


# might consider:
# description (string)
# colorId (string)
# location (string)
EVENT = {
    'summary': 'lol', # ,<- title
    'description': 'lolol',
    'location': '10332 Adobe Cir, Irvine, CA',
    'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
    'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
}


if __name__ == "__main__":
    creds = authenticate()
    calendar = getCalendar(creds)
    create_event_in_calendar(calendar, EVENT)