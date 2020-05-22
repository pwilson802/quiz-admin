from app import app
from flask import Flask, render_template, flash, request, redirect, url_for
from app.forms import LoginForm

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')