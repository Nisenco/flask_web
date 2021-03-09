from app import db
from datetime import datetime


# from app.notes.model import Message

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), unique=True)
#     body = db.Column(db.Text)
#     comment = db.relationship('Comment', back_populates='post')
#
#
# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text)
#     post_id = db.Column(db.Integer, db.ForeignKey('post_id'))
#     post = db.relationship('Post', back_populates='comments')
