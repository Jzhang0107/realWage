from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputForm

@app.route('/')
@app.route('/index')
def index():
    data = {'wage': '10000', 'city1': 'New York', 'city2': 'Boston'}     
    return render_template('index.html', data = data)

@app.route('/input', methods = ['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        #flash('Wage requested: {}, City 1: {}, City 2: {}'.format(
            #form.wage.data, form.city1.data, form.city2.data))
        return redirect(url_for('result'))
    return render_template(input.html, form = form)

@app.route('/result'):
def result():
