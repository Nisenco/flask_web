from flask import Flask
from flask_bootstrap import Bootstrap
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager, current_user
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect
from flask_babel import _, Babel

# 添加数据库
db = SQLAlchemy()

# 迁移数据库
migrate = Migrate()

# 加载插件
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
babel = Babel()
# 富文本插件
ckeditor = CKEditor()
csrf = CSRFProtect()