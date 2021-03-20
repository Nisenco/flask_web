from flask import redirect, url_for, render_template, flash, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from app.bluelog.model import Admin
from app.bluelog.form import LoginForm
from app.utils import redirect_back
from app.extensions import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
            return redirect(url_for('auth.register'))
    return render_template('auth/login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            flash('account is exist')
        else:
            register_admin = Admin(
                username=username,
                blog_title='',
                blog_sub_title="",
                name='',
                about=''
            )
            register_admin.set_password(password)
            db.session.add(register_admin)
            db.session.commit()
            flash("it's successful to register a account ", "info")
        redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect_back()
