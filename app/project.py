from app import app
from app.models import separate
from flask import render_template
from flask import request

@app.route('/')
@app.route('/startpage')
def startpage():
    user = {'name': 'Suraj', 'age': '34', 'pets': '7'}
    return render_template('startpage.html', title='Home', user=user)

@app.route('/separator', methods=['GET', 'POST'])
def separator():
    if request.method == 'GET':
        return "You're getting the results page!"
    else:
        userdata = dict(request.form)
        user_string = str(userdata)
        broken = separate.arrange(userdata['sentence'])
        broken_length = len(broken)
        return render_template('separator.html', len = broken_length, broken = broken)
