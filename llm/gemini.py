import google.generativeai as genai
from googleapiclient.discovery import build

user_input = "i want to schedule a list of events for 1/27. laundry will take 1 hour, i have a 2 hour hack at uci meeting from 2-3pm"

genai.configure(api_key="AIzaSyCXonLZeuV_Iy44XFKc8Q6P3x-QgonD16s")

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("""this is the format for an event object: event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google's developer products.',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

for each event identified in the following string, generate a list of these event objects in python. 

string = i want to schedule a list of events for 1/27. laundry will take 1 hour, i have a 2 hour meeting from 2-3pm""")

print(response.text)