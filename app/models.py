from app import db
from sqlalchemy import Sequence

class User(db.Model):
    id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Posts', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.nickname


class Posts(db.Model):
    id = db.Column(db.Integer, Sequence('post_id_seq'), primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.body