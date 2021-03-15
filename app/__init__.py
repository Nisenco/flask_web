from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager, current_user
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect
from flask_babel import _, Babel

app = Flask(__name__)
# 需要先添加数据库的配置项 然后添加数据库 先后顺序不能弄反

# 给app 添加配置项
app.config.from_object(Config)
# 添加数据库
db = SQLAlchemy(app)

# 迁移数据库
migrate = Migrate(app, db)

# 加载插件
login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'
bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)
babel = Babel(app)
# 富文本插件
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)

# 添加 蓝图
#  此处 app 不能提升至顶层
from app.notes import bp as notes_bp
from app.bluelog.routes.admin import admin_bp
from app.bluelog.routes.auth import auth_bp
from app.bluelog.routes.blog import blog_bp
# todolist项目
from app.todoism.routes.user import user_bp
from app.todoism.routes.todo import todo_bp
from app.todoism.routes.home import home_bp

# from app.auth import bp as auth_bp
# app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(notes_bp, url_prefix='/notes')
app.register_blueprint(blog_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(todo_bp)
app.register_blueprint(home_bp, url_prefix='/home')

# from app import models
from app.models import Admin, Category, Link, Comment, Item


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


# def register_template_todo_context(app):
#     @app.context_processor
#     def make_template_context():
#         if current_user.is_authenticated:
#             active_items = Item.query.with_parent(current_user).filter_by(done=False).count()
#         else:
#             active_items = None
#         return dict(active_items=active_items)


register_template_context(app)
# register_template_todo_context(app)
