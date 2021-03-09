from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment

app = Flask(__name__)
# 需要先添加数据库的配置项 然后添加数据库 先后顺序不能弄反

# 给app 添加配置项
app.config.from_object(Config)

# 添加数据库
db = SQLAlchemy(app)

# 迁移数据库
migrate = Migrate(app, db)


# 加载插件
bootstrap = Bootstrap(app)
mail = Mail(app)
moment = Moment(app)

# 添加 蓝图
from app.auth import bp as auth_bp
from app.notes import bp as notes_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(notes_bp, url_prefix='/notes')


from app import models
