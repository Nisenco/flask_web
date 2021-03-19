from flask import flash, redirect, url_for, render_template
from app.extensions import db
from app.notes.forms import NotesForm
from app.notes.model import Message
from app.notes import bp as notes_bp


@notes_bp.route('/', methods=['GET', 'POST'])
def notes_index():
    # 加载所有记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    notesForm = NotesForm()
    if notesForm.validate_on_submit():
        name = notesForm.name.data
        body = notesForm.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('your message have been sent')
        return redirect(url_for('notes.notes_index'))
    return render_template('notes/index.html', form=notesForm, messages=messages)
