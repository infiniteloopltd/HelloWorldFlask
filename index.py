import constants
from flask import Flask
import requests 
from scrapy.selector import Selector

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/hello')
def hello():
    # Render the page
    # message = "Hello World!"
    return constants.message

@app.route('/user/<id>/')
def user(id):
    return "Profile page of user #{}".format(id)

@app.route("/ip")
def ip():
    html = requests.get(url = "https://whatsmyip.com")    
    ip = Selector(text=html.content).css('[id="shownIpv4"]::text').get()
    return ip

if __name__ == '__main__':
    # Run the app server on localhost:4444
    app.run('localhost', 4444)
