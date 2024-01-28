# builds off of functioncalltest.py <-- mostly just experiment

import google.generativeai as genai
import google.ai.generativelanguage as glm

genai.configure(api_key="AIzaSyCXonLZeuV_Iy44XFKc8Q6P3x-QgonD16s")

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
                required=["start", "end"]
            )
        )
    ]
)

model = genai.GenerativeModel("gemini-pro", tools=[schedule_event_tool])

# is there any way to send these as the "system", like how OpenAI does?

prompting_messages = [
    "If an event location is not specified, infer the location within reason. For example, chores are probably done at home.",
    "If the event start and end times are not specified, pick reasonable ones based on the user-provided description.",
    "No need to ask for confirmation; the user will manually edit whatever you generate if needed.",
    "Schedule the following event: "
]

def get_event_object(user_prompt: str):

    chat = model.start_chat()
    
    for m in prompting_messages:
        chat.send_message(m)

    response = chat.send_message(user_prompt)

    return response.candidates[0].content.parts[0].function_call


# print(get_event_object("I am going to Matthew's apartment to celebrate his birthday at 12 pm."))
# print(get_event_object("I have to do laundry sometime in the evening."))




    




