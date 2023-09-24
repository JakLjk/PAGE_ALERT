from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User
from .tools.sign_up_verify import verify_password
from page_alert.metadata.custom_exceptions.webapp_exceptions import PasswordIntegrityException


auth = Blueprint('auth', __name__)

@auth.route("sign-in", methods=["GET","POST"])
def sign_in():
    if request.method == "POST":
        email = request.form.get('inputEmail')
        password = request.form.get('inputPassword')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.pages_list'))
            else:
                flash("Incorrect login information, try again.", category='error')
        else:
            flash('Incorrect login information, try again.', category='error')
    return render_template('sign_in.html', user=current_user)

@auth.route("logout")
def logout():
    logout_user()
    return redirect(url_for('auth.sign_in'))

@auth.route("sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('inputEmail')
        password1 = request.form.get('inputPassword1')
        password2 = request.form.get('inputPassword2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Use different email.", "error")
        else:
            try:
                verify_password(password1, password2)
                new_user = User(
                    email=email,
                    password=generate_password_hash(password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('Account created!', category='success')
                login_user(new_user, remember=True)
                return redirect(url_for('views.pages_list'))
            except PasswordIntegrityException as pie:
                flash(str(pie), "error")
    return render_template("sign_up.html", user=current_user)