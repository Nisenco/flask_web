from app import db
from datetime import datetime


class Message(db.Model):
    __tablename__ = 'Message'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
