from urllib import request
from flask import Blueprint, render_template




views = Blueprint('views', __name__)

@views.route('/')
def about():
    return render_template("index.html")


@views.route('/experience')
def experience():
    return render_template("experience.html")


@views.route('/projects')
def projects():
    return render_template("projects.html")


@views.route('/contact')
def contact():
    return render_template("contact.html")


@views.route('/luffy')
def contact():
    return render_template("db.html")