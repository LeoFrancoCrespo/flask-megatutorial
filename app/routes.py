from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm 

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

@app.route('/login') 
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data 
        remember_me = form.remember_me.data 
        flash(f'Login requested for user {username}, remember_me={remebmer_me}') 
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)