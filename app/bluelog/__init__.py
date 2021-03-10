from flask import Blueprint

blog_bp = Blueprint('blog', __name__)
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)

from app.bluelog import routes
