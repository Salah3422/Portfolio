from app import app
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy(app)


class Email(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email_address = db.Column('email_address', db.String(100))
    subject = db.Column('subject', db.String(100))
    message = db.Column('message', db.Text(1000))

    def __init__(self, name, email_address, subject, message):
        self.name = name
        self.email_address = email_address
        self.subject = subject
        self.message = message

    def __repr__(self):
        return self.name