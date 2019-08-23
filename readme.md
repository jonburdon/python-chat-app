# Flask Chat Room App
This is a chat app written in Flask.

# Project Aims
* Create and run flask project
* Take data from URLs and Store
* Present stored data back to user
* Create URLs based around user names
* When user Adds a message, this will be displayed along with a timestamp

## Approach

## Basic Setup

### Setup using VS Code on a Mac
* **sudo pip3 install Flask** to install Flask
* **python3 -m venv env** to install virtual environment in that folder
* Open command pallette, type **Python: Select Interpreter** and select the virtual environment in your project folder that starts with ./env or .\env
* In command pallette, run **Terminal: Create New Integrated Terminal**
* Install Flask in the virtual environment with **pip3 install Flask**
* Create app.py (In flask, the convention is to use run.py or app.py)
* **from flask import Flask** to import Flask in app.py Capital F indicates a class name.
* Create instance of flash within app.py with **app = Flask(name)**
* In Terminal **python3 -m flask run** to run the app and serve

* **pip3 freeze --local > requirements.txt** 

### Adding Views
* Add username route using variable. Note <> indicates variables.
* Check this works by browsing to http://127.0.0.1:5000/myname
* Should display **Hi myname**

* Add message route to app.py
* Check this works by browsing to: http://127.0.0.1:5000/fred/mymessage
* Should display **fred: mymessage**

### Storing messages in lists
* Create messages list
* Create add_messages function
* Update line 19 to return data from the list
* Test by checking as before
* import redirect from Flask library
* call add_messages function in send_message function
* Update user function to display messages
* Check **http://127.0.0.1:5000/kate/hello everyone** redirects to **http://127.0.0.1:5000/kate**, and displays **Welcome, kate - ['kate: hello everyone']**

### Displaying messages in more friendly format
* Create get_all_messages function and call it from user function. This will use <br> tags to separate each new message.

## Expanding functionality

### Adding timestamps
* In app.py use **from datetime import datetime** to import datetime
* Use strf time method in line 10 to convert date time obeject into string - use brackets to provide format
* Test

### Creating index.html
* import render_template from Flask
* Edit index view to return render_template("index.html")
* Test

### Creating users
* Use Flask to create session cookie and store username
* Import request and session module from Flask
* Create secret key (use string, but for production this would be an environment variable)
* Create form in index.html
* Allow GET and POST in index route
* Use if loop to assign input from form to username variable and store as session variable as session cookie

### Storing in a dictionary
* Refactor add_messages function to store in dictionary so that different messages can easily be accessed.
* Removed get_all_messages function - no longer needed

### Create template for chats to display dictionary data
* Create chat.html and use render_template to load it.
* Use Jinja to display data from message dictionary.
* Add Javascript to auto reload

### Create a message textbox for user input
* Add form to chat.html for message input.
* Update username route in app.py to permit GET and POST methods
* Add if function to username route to receive form input and assign variables
* Refactor javascript to stop it refreshing whilst form is being completed.

## Future Plans
* Use css to add 'bubble' theme for each new message
* Vary the above to alternate colour of each new chat 'bubble'