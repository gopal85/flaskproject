from app import app
from app.models import model
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Suraj'}
    return render_template('index.html', title='Home', user=user)

@app.route('/secret')
def secret():
    name = "Suraj"
    return "<h1>Hello " + name + "!</h1>"

@app.route('/welcome')
def welcome():
    name = "Upperline"
    return "<h1>Hello, and welcome to " + name + "!</h1>"

@app.route('/goodbye')
def goodbye():
    return "<h2>That's the end of our time together.</h2>"

@app.route('/resultspage')
def resultspage():
    user = {'name': 'Gopi', 'pets': '7'}
    return render_template('resultspage.html', title='On the Run', user=user)

@app.route('/sendBreakfast', methods=['GET', 'POST'])
def handleBreakfast():
    if request.method == 'GET':
        return "You're getting the breakfast page!"
    else:
        userdata = dict(request.form)
        nickname = model.shout(userdata['nickname'])
        breakfast = model.shout(userdata['breakfast'])
        return "Hello, " + nickname + ", I heard you had " + breakfast + " for breakfast! Sounds delicious."
