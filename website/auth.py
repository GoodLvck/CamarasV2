from crypt import methods
from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)


# -------------------- Login --------------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/es/login', methods=['GET', 'POST'])
def loginES():
    return render_template("loginES.html")


# -------------------- Signup --------------------
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(username) < 3:
            flash('Username must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("signup.html")


# -------------------- Logout --------------------
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
