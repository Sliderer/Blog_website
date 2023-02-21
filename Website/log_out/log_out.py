from flask import Blueprint, render_template

log_out = Blueprint('log_out_user', __name__, template_folder='templates', static_folder='static')


@log_out.route('/')
def home_page():
    return render_template('home_page.html')
