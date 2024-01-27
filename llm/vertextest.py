import vertexai

# This entire thing may only work for Rutvik
# (I installed Google Cloud CLI and authenticated myself through it. Not sure if everyone on the project needs to do that,
# or if it just works for everyone added to the project.)

# this one seems more powerful but needs more wrangling / prompt engineering.
# seems reluctant to actually use the created tool.

# do not bother with this lol

vertexai.init(project="auto-scheduler-399002")

from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel

model = GenerativeModel("gemini-pro")


get_current_weather_func = generative_models.FunctionDeclaration(
  name="get_current_weather",
  description="Get the current weather in a given location",
  parameters={
      "type": "object",
      "properties": {
          "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
              "type": "string",
              "enum": [
                  "celsius",
                  "fahrenheit",
              ]
          }
      },
      "required": [
          "location"
      ]
  },
)

calendar_insert_func = generative_models.FunctionDeclaration(
    name="calendar_insert_func",
    description="insert an event into Google calendar",
    parameters= {
        "type" : "object",
        "properties" : {
            "location" : {
                "type": "string",
                "description": "The location the event will occur"
            },
            "start" : {
                "type" : "string",
                "description" : "Datetime format; the time the event starts"
            },
            "end" : {
                "type" : "string",
                "description" : "Datetime format; the time the event ends"
            }
        },
        "required" : ["start", "end"]
    }

)

weather_tool = generative_models.Tool(
  function_declarations=[get_current_weather_func]
)

calendar_tool = generative_models.Tool(
    function_declarations=[calendar_insert_func]
)

# model_response = model.generate_content(
#     "I have a 2 hour meeting at 3pm today for Aprilia aero research. Can you insert this into my google calendar",
#     generation_config={"temperature": 0},
#     tools=[calendar_tool],
# )

# print("model_response\n", model_response)

chat = model.start_chat()

chat.send_message("No need to ask for confirmation. the user will manually fix things if needed. Assume you have access to client's google calendar")

response = chat.send_message("I have a meeting from 2pm to 4pm for Honda chassis research. Can you add this to my google calendar?", tools=[calendar_tool])

print(response)