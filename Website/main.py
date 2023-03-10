from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash, session
from flask_login import login_required, LoginManager, login_user
from secret_key_generator import SecretKeyGenerator
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from log_out import log_out
from log_in import log_in

from models import UserLogin
from config import database

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(log_out, url_prefix='/logout')
app.register_blueprint(log_in, url_prefix='/login')


@login_manager.user_loader
def load_user(user_id):
    return database.find_user_by_id(user_id)


@app.route('/')
def log_out_user():
    if 'used_id' in session:
        load_user(session['used_id'])
        return redirect('/login')
    return redirect('/logout')


@app.route('/')
@login_required
def log_in_user():
    return redirect('/login')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html', links=['/logout', '/registration', '/registration'])
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if len(name) < 3:
            flash('Your name is too short')
            return redirect('/registration')

        if len(password) < 3:
            flash('Your password is too short')
            return redirect('/registration')

        password = generate_password_hash(password)
        temp_user = UserLogin().init_for_registration(name, password, email)
        user = database.add_user(temp_user)

        if user:
            login_user(user)
            session.permanent = True
            session['used_id'] = user.id
            return redirect('/login')
        else:
            return redirect(url_for('register'))


@app.route('/enter', methods=['GET', 'POST'])
def enter():

    if request.method == 'GET':
        return render_template('enter.html', links=['/logout', '/enter', '/enter'])
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = database.find_user_by_email(email)

        if not user:
            flash('Unknown email')
            return redirect(url_for('enter'))

        if check_password_hash(user.password, password):
            login_user(user)
            session.permanent = True
            session['used_id'] = user.id
            return redirect('/login')
        else:
            flash('Wrong password')
            return redirect(url_for('enter'))


if __name__ == '__main__':
    secret_key = SecretKeyGenerator.generate_secret_code()
    app.secret_key = secret_key
    app.run(debug=True)
