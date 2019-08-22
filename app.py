import os
from datetime import datetime
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))

def get_all_messages():
    """Get all messages and separate using a <br>"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instructions"""
    return "Instructions: To send a message use /USERNAME/MESSAGE"

"""<anything here> will be treated as a variable"""
@app.route('/<username>')
def user(username):
    """Display chat page"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redirect to chat page"""
    add_messages(username, message)
    return redirect("/" + username)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)