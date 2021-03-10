from flask import redirect, url_for, render_template, flash
from app.bluelog import auth_bp, blog_bp, admin_bp
from flask_login import login_user, logout_user, login_required, current_user


# blog 路由
@blog_bp.route('/')
def index():
    return render_template('blog/index.html')


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    return render_template('blog/category.html')


@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    return render_template('blog/post.html')


# auth 用户路由
@auth_bp.route('/')
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '登录页面'


@auth_bp.route('/logout')
def logout():
    return '用户登出'


# admin_bp 管理员页面
@admin_bp.route('/')
def index():
    return '管理员首页'
