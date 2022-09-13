from urllib.request import Request
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/about')
def home():
    return render_template("about.html")


@views.route('/experience')
def experience():
    return render_template("experience.html")


@views.route('/projects')
def projects():
    return render_template("projects.html")

@views.route("/contact", methods=['GET', 'POST'])
def contact():
        return render_template("contact.html")



'''
@views.route("/contact/<text>", text="Thank you!", methods=['GET', 'POST'])
def contact(text):
    if Request.method == "POST":
        return render_template("/contact/<text>")
    else:
        return render_template("contact.html")
'''  

