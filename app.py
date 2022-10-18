import os
import sys

from flask import Flask, render_template, request
#from models import db, Email
from flask_sqlalchemy import SQLAlchemy

sys.path.append("..")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is the secret key *change later*'

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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





@app.route('/')
def about():
    return render_template("index.html")


@app.route('/experience')
def experience():
    return render_template("experience.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")
    

@app.route('/contact_submission', methods=['POST'])
def contact_submission():
    error_statement = "Please fill out all required fields."
    success_statement = "Thank you for your submission"

    if request.method == "POST":
        name = request.form['name']
        email_address = request.form['email_address']
        subject = request.form['subject']
        message = request.form['message']
        
        email = Email(name=name, email_address=email_address, subject=subject, message=message)
        print(email.name, email.email_address, email.subject, email.message)

        #server = smtplib.SMTP("smtp.gmail.com", 587)
        #server.starttls()
        #server.login("salahzahranai@gmail.com", "zahran1211")
        #server.sendmail(email.name, "salahzahranai@gmail.com", email.message)
        
        if not name or not email_address or not message:
            return render_template('contact.html', error_statement=error_statement)
        else:
            try:
                db.session.add(email)
                db.session.commit()
                print("Updating Database")         
            except:
                print("Failure!")
        
        return render_template('contact.html', success_statement=success_statement)  
        
    else:
        emails = Email.query.order_by(Email.id)
        return render_template('contact.html')



@app.route('/database')
def database():
    emails = Email.query.all()
    return render_template("db.html", emails=emails)



if __name__ == '__main__':
    with app.app_context():     
        db.create_all()
    app.run(debug=True)