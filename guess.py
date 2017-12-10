#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from flask import Flask, session, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class GuessNumberForm(FlaskForm):
    number = IntegerField('Input an integer (1 ~ 1000)', validators=[
        DataRequired('Input a valid integer!'),
        NumberRange(1, 1000, 'Input an integer between 1 ~ 1000!')])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'something hard to guess'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session['number'] = randint(1, 1000)
    session['times'] = 10
    result = session.get('result', None)
    session['result'] = None
    return render_template('index.html', result=result)


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    times = session['times']
    result = session['number']
    form = GuessNumberForm()
    if form.validate_on_submit():
        session['result'] = result
        times -= 1
        session['times'] = times
        if times == 0:
            flash('You failed.', 'danger')
            return redirect(url_for('index'))
        answer = form.number.data
        if answer > result:
            flash("Too big. You still have {} times.".format(times), 'warning')
        elif answer < result:
            flash("Too small. You still have {} times.".format(times), 'info')
        else:
            flash('Congratulations! You made it!', 'success')
            return redirect(url_for('index'))
        return redirect(url_for('guess'))
    return render_template('guess.html', form=form)