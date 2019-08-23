import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomstring123321"
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)


@app.route('/', methods= ["GET", "POST"])
def index():
    """Main page with instructions"""
    """Get username from form"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    """If username exists, redirect to username route"""
    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

"""<anything here> will be treated as a variable"""
@app.route('/<username>', methods = ["GET", "POST"])
def user(username):
    """Display chat page"""

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_messages(username, message)
        """Use redirect to avoid continually adding the message."""
        return redirect(session["username"])

    return render_template("chat.html", username = username, chat_messages = messages)

@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create a new message and redirect to chat page"""
    add_messages(username, message)
    return redirect("/" + username)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)