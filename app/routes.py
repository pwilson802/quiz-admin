from app import app
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.urls import url_parse
from app.forms import LoginForm
from flask_login import login_required
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.mod import get_question_api, add_question, get_question_csv, get_all_qq_questions

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('qq_add'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('qq_add')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('qq_add'))


@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
@login_required
def index():
    return render_template('index.html')


@app.route('/qq_index', methods=["GET"])
@login_required
def qq_index():
    data = get_all_qq_questions()
    return render_template('qq_index.html', data=data)


@app.route('/qq_add', methods=["POST", "GET"])
@login_required
def qq_add():
    if request.method == 'POST':
        request_type = request.values.get('action')
        if request_type == 'get_question_api':
            category = request.values.get("category")
            difficulty = request.values.get("difficulty")
            data = get_question_api(category, difficulty)
            data['source'] = 'api'
            return render_template('qq_add.html', data=data)
        if request_type == 'get_question_csv':
            data = get_question_csv()
            data['source'] = 'csv'
            return render_template('qq_add.html', data=data)
        if request_type == 'post_question':
            print(request.values.to_dict())
            question_dict = request.values.to_dict()
            add_q = add_question(question_dict)
            if add_q['response'] == 'already_exists':
                # This looks really bad and should be fixed
                flash('Question is already in the database')
            #post the question to dynamodb and give a response
            return render_template('qq_add.html')
    else:
        return render_template('qq_add.html')