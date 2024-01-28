# builds off of functioncalltest.py <-- mostly just experiment

import google.generativeai as genai
import google.ai.generativelanguage as glm

genai.configure(api_key="AIzaSyCXonLZeuV_Iy44XFKc8Q6P3x-QgonD16s")

def generate_model():
    schedule_event_tool = glm.Tool(
        function_declarations= [
            glm.FunctionDeclaration(
                name="schedule_event",
                description="Inserts an event into a google calendar",
                parameters= glm.Schema(
                    type=glm.Type.OBJECT,
                    properties= {
                        "summary" :     glm.Schema(type=glm.Type.STRING, description="Title for the event"),
                        "description" : glm.Schema(type=glm.Type.STRING, description="casual Gemini generated description of the event with some detail."),
                        "location" :    glm.Schema(type=glm.Type.STRING, description="Specific location where the event will take place. Examples: home, office, Matthew's apartment"),
                        "start" :       glm.Schema(type=glm.Type.STRING, description="String in datetime format to be used by a program for when the event begins"),
                        "end" :         glm.Schema(type=glm.Type.STRING, description="String in datetime format to be used by a program for when the event ends")
                    },
                    required=["summary" ,"description", "location", "start", "end"]
                )
            )
        ]
    )

    model = genai.GenerativeModel("gemini-pro", tools=[schedule_event_tool])
    return model

# is there any way to send these as the "system", like how OpenAI does?

def get_event_object(model, user_prompt: str):
    print("getting call")
    prompting_messages = [
    "If an event location is not specified, infer the location within reason. For example, chores are probably done at home.",
    "Do not ask the user for further information. It is OK to infer anything reasonable."
    "If the event start and end times are not specified, pick reasonable ones based on the user-provided description. Scheduling an event with an unspecified time for today is acceptable.",
    "DO NOT ask the user for confirmation. Just try to schedule the event on the calendar. The user will manually edit whatever is generated if needed.",
    "Output times in the API datetime format to be used by a program.",
    "Today is February 1, 2024 and the current timezone is Pacific Standard Time."
    "Schedule the following event: "
]

    chat = model.start_chat()
    print("chat value: ", chat)
    
    for m in prompting_messages:
        chat.send_message(m)

    response = chat.send_message(user_prompt)

    print("TYPE", type(response.candidates[0].content.parts[0].function_call))

    while (response.candidates[0].content.parts[0].function_call.args["summary"] == None):
        response = chat.send_message("yes")

    print("return value: ", response.candidates[0])
    return response.candidates[0].content.parts[0].function_call


# print(get_event_object("I am going to Matthew's apartment to celebrate his birthday at 12 pm."))
# print(get_event_object("I have to do laundry sometime in the evening."))




    




