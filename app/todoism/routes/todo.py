from faker import Faker
from flask import render_template, redirect, url_for, Blueprint, request, jsonify
from flask_babel import _
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.todoism.model import User, Item

todo_bp = Blueprint('todo', __name__)


@todo_bp.route('/app')
@login_required
def app():
    return 'app'


@todo_bp.route('/items/new', methods=['POST'])
@login_required
def new_item():
    data = request.get_json()
    if data is None or data['body'].strip() == '':
        return jsonify(message=_('Invalid item body.')), 400
    item = Item(body=data['body'], author=current_user._get_current_object())
    db.session.add(item)
    db.session.commit()
    return jsonify(html=render_template('todoism/_item.html', item=item), message='+1')


@todo_bp.route('/item/clear', methods=['DELETE'])
@login_required
def clear_items():
    items = Item.query.with_parent(current_user).filter_by(done=True).all()
    for item in items:
        db.session.delete(item)
    db.session.commit()
    return jsonify(message=_('All clear!'))
