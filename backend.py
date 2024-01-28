from auth_calendar import create_event_in_calendar
from llm.create_event import generate_model, get_event_object




# print("function_call_obj:", function_call_obj)



# EVENT = {
#     'summary': 'lol', # ,<- title
#     'description': 'lolol',
#     'location': '10332 Adobe Cir, Irvine, CA',
#     'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
#     'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
# }
# print("\nevent obj: ", event_obj)
# event = create_event_in_calendar(calendar, event_obj)
# print("\nEvent: ", event)


def add_event_to_calendar(event_to_create, calendar):

    model = generate_model()

    function_call_obj = get_event_object(model, event_to_create)

    summary = function_call_obj.args['summary']
    description = function_call_obj.args['description']
    location = function_call_obj.args['location']
    start = function_call_obj.args['start']
    end = function_call_obj.args['end']

    event_obj = {
        'summary': summary, # ,<- title
        'description': description + "\n Added by LLM Calendar Buddy",
        'location': location,
        'start': {'dateTime': start},
        'end': {'dateTime': end}
    }

    event = create_event_in_calendar(calendar, event_obj)

    return event