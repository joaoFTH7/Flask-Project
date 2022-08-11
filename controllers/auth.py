from flask import render_template, request, redirect, session, flash, url_for
from models.users import Users
from helpers.helpers import UserForm
from flask_bcrypt import check_password_hash


class AuthController:
    def login():
        user_form = UserForm()
        next = request.args.get("next")
        return render_template("auth/login.html", next=next, form_user=user_form)

    
    def auth():
        form_user = UserForm(request.form)

        user = Users.query.filter_by(nick=form_user.nick.data).first()
        user_pass = check_password_hash(user.password, form_user.password.data)
        if user and user_pass:
            session['logged_user'] = request.form['nick']
            flash(f"Welcome {request.form['nick']}!")
            next_page = request.form['next']
            if next_page:
                return redirect(url_for("hello"))
            else:
                return redirect(next_page)
        else:
            flash("username or password incorrect")
            return redirect(url_for("login"))


    def logout():
        session['logged_user'] = None
        flash("Logout successfully")
        return redirect(url_for("login"))