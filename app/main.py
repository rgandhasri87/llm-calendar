from app import app
from flask import request, render_template
import auth_calendar


sample_event_body = {
        'summary': 'lol',
        'description': 'lolol',
        'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
        'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
}


@app.route('/', methods=['GET', 'POST'])
def index():
    creds = auth_calendar.authenticate()
    calendar_embed_url = r'https://calendar.google.com/calendar/embed?src=susannl5@uci.edu'

    if request.method == "POST":
        prompt = request.form.get("comment")
        print(prompt)
    return render_template("calendar.html", calendar_embed_url = calendar_embed_url)