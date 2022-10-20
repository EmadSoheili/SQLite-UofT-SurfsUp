# Import Dependencies
from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# Create a route
@app.route('/')
def hello_world():
    return 'Hello World!'
