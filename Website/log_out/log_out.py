from flask import Blueprint, render_template

log_out = Blueprint('log_out_user', __name__, template_folder='templates', static_folder='static')


@log_out.route('/')
def home_page():
    print('logout')
    return render_template('logout_home_page.html', links=['/', '/registration', '/registration'])
