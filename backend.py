from auth_calendar import getCalendar, authenticate, create_event_in_calendar
prompt = input()


creds = authenticate()
calendar = getCalendar(creds)



create_event_in_calendar(calendar, event)

