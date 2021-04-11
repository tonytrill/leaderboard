from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    leaderboard = db.relationship('Leaderboard', 'owner', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.email}>'

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    name = db.Column(db.String(120))

    def __repr__(self):
        return f'<Leaderboard {self.name}>'