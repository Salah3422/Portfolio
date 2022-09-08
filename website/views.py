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


@views.route('/contact')
def contact():
    return render_template("contact.html")