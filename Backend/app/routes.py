from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    data = {'wage': '10000', 'city1': 'New York', 'city2': 'Boston'}     
    return render_template('index.html', data = data)