from flask import Flask, render_template

app = Flask("Calendar", static_folder='staticFiles')

@app.route('/')
def calendar():
    user_email = "susannl5@uci.edu" #placement
    calendar_embed_url = f'https://calendar.google.com/calendar/embed?src={user_email}'
    return render_template('calendar.html', calendar_embed_url=calendar_embed_url)

if __name__ == '__main__':
    app.run(debug=False)

