import google.generativeai as genai
import google.ai.generativelanguage as glm

# from googleapiclient.discovery import build

# following: https://ai.google.dev/tutorials/function_calling_python_quickstart
# and not the vertex api one


genai.configure(api_key="AIzaSyCXonLZeuV_Iy44XFKc8Q6P3x-QgonD16s")


tool = glm.Tool(
    function_declarations= [
        glm.FunctionDeclaration(
            name="schedule_event",
            description="Inserts an event into a google calendar",
            parameters= glm.Schema(
                type=glm.Type.OBJECT,
                properties= {
                    "description" : glm.Schema(type=glm.Type.STRING, description="Gemini generated description of the event"),
                    "location" : glm.Schema(type=glm.Type.STRING, description="Specific location where the event will take place. Examples: home, office, Matthew's apartment"),
                    "start" : glm.Schema(type=glm.Type.STRING, description="String in datetime format for when the event begins"),
                    "end" : glm.Schema(type=glm.Type.STRING, description="String in datetime format for when the event ends")
                },
                required=["start", "end"]
            )
        )
    ]
)

model = genai.GenerativeModel('gemini-pro', tools=[tool])

chat = model.start_chat()

# prompt engineering whatever

# currently can only schedule one thing at a time. future improvement could be putting multiple events in a message.

chat.send_message("Infer the location of events within reason. For example, if I have to cook dinner, it is reasonable to infer i will cook at home")
chat.send_message("I need you to schedule the following event.")

response = chat.send_message("Laundry sometime in the evening.")

print(response.candidates[0])
print("|             |                       |")
fc = response.candidates[0].content.parts[0].function_call

# assert fc.name == "schedule event"

print(fc)
