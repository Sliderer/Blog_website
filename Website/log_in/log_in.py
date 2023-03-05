from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import login_required, current_user
from models import UserLogin, Blog
from config import database

log_in = Blueprint('login', __name__, template_folder='templates', static_folder='static')

@log_in.route('/')
@login_required
def login_home():
    username = current_user.get_name()
    return render_template('login_home_page.html', user_name=username)


@log_in.route('/create_blog', methods=['GET', 'POST'])
@login_required
def create_blog():
    if request.method == 'GET':
        return render_template('create_blog.html')
    else:
        title = request.form.get('title')
        text = request.form.get('text')
        blog = Blog().init_form_creation(title, text)

        database.add_user_blog(current_user.get_id(), blog)

        flash('Your blog posted!')
        return redirect(url_for('.create_blog'))

@log_in.route('/blogs')
@login_required
def top_blogs():
    return "Blogs"


@log_in.route('/my_blogs', methods=['GET', 'POST'])
@login_required
def user_blogs():
    if request.method == 'GET':
        blogs = database.get_user_blogs(current_user)
        return render_template('my_blogs.html', blogs=blogs)
    else:
        return redirect(url_for('.create_blog'))


@log_in.route('/account')
@login_required
def account():
    return render_template('account.html', current_user=current_user)
