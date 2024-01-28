from auth_calendar import getCalendar, authenticate, create_event_in_calendar
from llm.create_event import generate_model, get_event_object

prompt = input("Please list out the events you want scheduled in your calendar. ")

creds = authenticate()
calendar = getCalendar(creds)

model = generate_model()
print("model:", model)
function_call_obj = get_event_object(model, prompt)

print("function_call_obj:", function_call_obj)

# fc object
# args {
#   fields {
#     key: "summary"
#     value {
#       string_value: "Laundry"
#     }
#   }
#   fields {
#     key: "start"
#     value {
#       string_value: "2022-05-18T20:00:00Z"
#     }
#   }
#   fields {
#     key: "end"
#     value {
#       string_value: "2022-05-19T02:00:00Z"
#     }
#   }
#   fields {
#     key: "description"
#     value {
#       string_value: "Do the laundry"
#     }
#   }
# }

summary = function_call_obj.args['summary']
description = function_call_obj.args['description']
start = function_call_obj.args['start']
end = function_call_obj.args['end']

print("START: ", start)
print("END: ", end)

event_obj = {
    'summary': summary, # ,<- title
    'description': description,
    'location': '10332 Adobe Cir, Irvine, CA',
    'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
    'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
}
# EVENT = {
#     'summary': 'lol', # ,<- title
#     'description': 'lolol',
#     'location': '10332 Adobe Cir, Irvine, CA',
#     'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
#     'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
# }
print("\nevent obj: ", event_obj)
event = create_event_in_calendar(calendar, event_obj)
print("\nEvent: ", event)

