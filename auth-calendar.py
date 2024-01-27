from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


# initiates OAuth 2.0 process & returns credentials
def authenticate():
    SCOPES = "https://www.googleapis.com/auth/calendar"
    store = file.Storage("storage.json")
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    return tools.run_flow(flow, store) # return credentials


# returns user's calendar
def getCalendar(credentials):
    return build('calendar', 'v3', http=credentials.authorize(Http()))


# creates event in calendar & returns event
def create_event_in_calendar(calendar, body, calendarId='primary', sendNotifications=True):
    try:
        event = calendar.events().insert(calendarId=calendarId, sendNotifications=sendNotifications, body=body).execute()
        print(f"successfully created event with body {body}")
        return event
    except:
        print(f"failed to create event with body {body}")
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

EVENT = {
    'summary': 'lol2',
    'location': '10332 Adobe Cir, Irvine, CA',
    'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
    'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
}

creds = authenticate()
calendar = getCalendar(creds)
create_event_in_calendar(calendar, EVENT)
