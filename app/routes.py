from flask import render_template, flash, redirect, get_flashed_messages, url_for
from app import app
from app.forms import LoginForm
from app import run


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/grandpy', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    message = {'said_by_grandpy': None}
    if form.validate_on_submit():
        flash('You asked GrandPy: {}'.format(
            form.username.data))
        user_input = get_flashed_messages()[0]
        grandpy_return = run.get_infos_on_place(user_input)
        message['said_by_grandpy'] = grandpy_return
        return redirect(url_for('login'))
    return render_template('grandpy.html', title='GrandPy', form=form, message=message)