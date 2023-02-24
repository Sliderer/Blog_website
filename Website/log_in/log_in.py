from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

from models import UserLogin

log_in = Blueprint('login', __name__, template_folder='templates', static_folder='static')



@log_in.route('/')
@login_required
def login_home():
    username = current_user.get_name()
    print(username)
    return render_template('login_home_page.html', links=[
    url_for('.login_home') + '/', url_for('.login_home') + 'blogs', url_for('.login_home') + 'my_blogs'],
                           user_name=username)


@log_in.route('/blogs')
@login_required
def blogs():
    return "Blogs"


@log_in.route('/my_blogs')
def user_blogs():
    return 'My blogs'


@log_in.route('/account')
def account():
    return render_template('account.html',
                           links=[url_for('.login_home') + '/', url_for('.login_home') + 'blogs', url_for('.login_home') + 'my_blogs'],
                           current_user=current_user)
