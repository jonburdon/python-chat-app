import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}: {}".format(username, message))

@app.route('/')
def index():
    """Main page with instructions"""
    return "Instructions: To send a message use /USERNAME/MESSAGE"

"""<anything here> will be treated as a variable"""
@app.route('/<username>')
def user(username):
    """Display chat page"""
    return "Welcome, {0} - {1}".format(username, messages)

@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redirect to chat page"""
    add_messages(username, message)
    return redirect("/" + username)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)