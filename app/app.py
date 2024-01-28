from flask import Flask, request, render_template
from backend import add_event
from auth_calendar import authenticate, get_calendar

app = Flask(__name__, static_folder='staticFiles')

sample_event_body = {
        'summary': 'lol',
        'description': 'lolol',
        'start': {'dateTime': '2023-03-24T19:00:00+01:00'},
        'end': {'dateTime': '2023-03-24T23:59:00+01:00'}
}


@app.route('/', methods=['GET', 'POST'])
def index():
    creds = authenticate()
    calendar = get_calendar(creds)

    if request.method == "POST":
        event_to_create = request.form.get("comment")
        event = add_event(event_to_create, calendar)

    return render_template("calendar.html")

if __name__ == '__main__':
    app.run(debug=True)