import os
import db_setting


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = db_setting.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = db_setting.SQLALCHEMY_TRACK_MODIFICATIONS
    SECRET_KEY = os.getenv('SECRET_KEY', 'a secret string')
    # blog 每页显示条数
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_COMMENT_PER_PAGE = 15
    BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    # todolist 页数配置
    TODOISM_ITEM_PER_PAGE = 20
    # 邮箱配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('SUCCESSW2M@163.com')
    MAIL_PASSWORD = os.environ.get('W2308090624M')


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass
