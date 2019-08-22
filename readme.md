# Flask Chat Room App
This is a chat app written in Flask.

# Project Aims
* Create and run flask project
* Take data from URLs and Store
* Present stored data back to user
* Create URLs based around user names
* When user Adds a message, this will be displayed along with a timestamp

## Approach

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