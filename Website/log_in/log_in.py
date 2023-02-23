from flask import Blueprint, render_template, url_for
from flask_login import login_required

log_in = Blueprint('login', __name__, template_folder='templates', static_folder='static')


@log_in.route('/')
@login_required
def account():
    print('login')
    return render_template('login_home_page.html', links=[
        url_for('.account') + '/', url_for('.account') + 'blogs', url_for('.account') + 'my_blogs'
    ])


