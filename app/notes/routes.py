from flask import flash, redirect, url_for, render_template, request
from flask import current_app
from flask_paginate import Pagination,get_page_parameter
from app.extensions import db
from app.notes.forms import NotesForm
from app.notes.model import Message
from app.notes import bp as notes_bp


@notes_bp.route('/', methods=['GET', 'POST'])
def notes_index():
    # 加载所有记录
    page = request.args.get(get_page_parameter(), 1, type=int)
    per_page = current_app.config['NOTES_POST_PER_PAGE']
    start = (page-1) * per_page
    end = start + per_page
    total = Message.query.order_by(Message.timestamp.desc()).count()
    pagination = Pagination(bs_version = 3,page=page,per_page=per_page,total=total)
    messages = Message.query.order_by(Message.timestamp.desc()).slice(start,end)
    notesForm = NotesForm()
    if notesForm.validate_on_submit():
        name = notesForm.name.data
        body = notesForm.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('your message have been sent')
        return redirect(url_for('notes.notes_index'))
    return render_template('notes/index.html', form=notesForm,
                           messages=messages, pagination=pagination,total=total)
