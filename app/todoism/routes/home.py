from flask import render_template, Blueprint

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    return render_template('todoism/index.html')


@home_bp.route('/intro')
def intro():
    return render_template('todoism/_intro.html')
