from flask import Flask, Blueprint, redirect, url_for, render_template
from flask_login import login_required
from secret_key_generator import SecretKeyGenerator

from log_out import log_out

app = Flask(__name__)

app.register_blueprint(log_out, url_prefix='/logout')


@app.route('/')
def log_out_user():
    return redirect('/logout')


@app.route('/')
@login_required
def log_int_user():
    return redirect('/login')


@app.route('/registration')
def register():
    return render_template('registration.html', links=['/logout', '/registration', '/registration'])


@app.route('/enter')
def enter():
    return render_template('enter.html', links=['/logout', '/enter', '/enter'])


if __name__ == '__main__':
    secret_key = SecretKeyGenerator.generate_secret_code()
    app.secret_key = secret_key
    app.run(debug=True)
