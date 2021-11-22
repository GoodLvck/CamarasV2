from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("baseLogin.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def signup():
    return "<p>sign Up</p>"