from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_required
from secret_key_generator import SecretKeyGenerator

from log_out import log_out
from log_in import log_in

app = Flask(__name__)

app.register_blueprint(log_out, url_prefix='/logout')
app.register_blueprint(log_in, url_prefix='/login')


@app.route('/')
def log_out_user():
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

        return redirect('/login')


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'GET':
        return render_template('enter.html', links=['/logout', '/enter', '/enter'])
    else:
        # print(request.form.get('email'))
        return redirect('/enter')


if __name__ == '__main__':
    secret_key = SecretKeyGenerator.generate_secret_code()
    app.secret_key = secret_key
    app.run(debug=True)
