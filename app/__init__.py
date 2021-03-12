from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager,current_user
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect


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
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)
# 富文本插件
ckeditor = CKEditor(app)
csrf = CSRFProtect(app)

# 添加 蓝图
#  此处 app 不能提升至顶层
from app.notes import bp as notes_bp
from app.bluelog.routes.admin import admin_bp
from app.bluelog.routes.auth import auth_bp
from app.bluelog.routes.blog import blog_bp
# from app.auth import bp as auth_bp
# app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(notes_bp, url_prefix='/notes')
app.register_blueprint(blog_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')

# from app import models
from app.models import Admin,Category,Link,Comment

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

register_template_context(app)