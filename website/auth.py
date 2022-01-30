from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)


# -------------------- Login --------------------
@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/es/login')
def loginES():
    return render_template("loginES.html")


# -------------------- Signup --------------------
@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/es/signup')
def signupES():
    return render_template("signupES.html")


# -------------------- Logout --------------------
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
