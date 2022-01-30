from crypt import methods
from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)


# -------------------- Login --------------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/es/login', methods=['GET', 'POST'])
def loginES():
    data = request.form
    print(data)
    return render_template("loginES.html")


# -------------------- Logout --------------------
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
