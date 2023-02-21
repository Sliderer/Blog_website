from flask import Flask, Blueprint, redirect, url_for
from secret_key_generator import SecretKeyGenerator

from log_out import log_out

app = Flask(__name__)

app.register_blueprint(log_out, url_prefix='/logout')

@app.route('/')
def log_out_user():
    return redirect('/logout')

if __name__ == '__main__':
    secret_key = SecretKeyGenerator.generate_secret_code()
    app.secret_key = secret_key
    app.run(debug=True)