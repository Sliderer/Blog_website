from flask import Flask, Blueprint
from secret_key_generator import SecretKeyGenerator

app = Flask(__name__)

if __name__ == '__main__':
    secret_key = SecretKeyGenerator.generate_secret_code()
    app.secret_key = secret_key
    app.run(debug=True)