from app import app
from app.auth.form import LoginForm
from flask import render_template, url_for, request


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
