from flask import Flask
from config import BaseConfig
from flask_login import LoginManager, current_user
from flask_babel import _, Babel
from app.extensions import db, migrate, login_manager, bootstrap, \
    mail, moment, babel, ckeditor, csrf
# 添加api 接口
from app.apis.v1 import api_v1
# 添加路由
from app.notes import bp as notes_bp
# 博客项目
from app.bluelog.routes.admin import admin_bp
from app.bluelog.routes.auth import auth_bp
from app.bluelog.routes.blog import blog_bp
# todolist项目
# from app.todoism.routes.user import user_bp
# from app.todoism.routes.todo import todo_bp
# from app.todoism.routes.home import home_bp
from app.models import Admin, Category, Link, Comment, Item


# 需要先添加数据库的配置项 然后添加数据库 先后顺序不能弄反
def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    register_extensions(app)
    register_buleprints(app)
    register_template_context(app)
    return app


def register_extensions(app):
    # 添加数据库
    db.init_app(app)

    # 迁移数据库
    migrate.init_app(app, db)

    # 加载插件
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    # 富文本插件
    ckeditor.init_app(app)
    csrf.init_app(app)


def register_buleprints(app):
    app.register_blueprint(notes_bp, url_prefix='/notes')
    app.register_blueprint(blog_bp,url_prefix='/blog')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    # app.register_blueprint(user_bp, url_prefix='/user')
    # app.register_blueprint(todo_bp)
    # app.register_blueprint(home_bp, url_prefix='/home')
    app.register_blueprint(api_v1, url_prefix='/api/v1')


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        links = Link.query.order_by(Link.name).all()
        if current_user.is_authenticated:
            unread_comments = Comment.query.filter_by(reviewed=False).count()
        else:
            unread_comments = None
        return dict(
            admin=admin, categories=categories,
            links=links, unread_comments=unread_comments)
