from flask import flash, redirect, session, url_for
from models.games import Games
from app.gamebrary import db

class DeleteGameController:
    def delete_game(id):
        if 'logged_user' not in session or session['logged_user'] == None:
            return redirect(url_for("login", next=url_for("hello")))
        gamename = Games.query.filter_by(id=id).first()
        Games.query.filter_by(id=id).delete()
        db.session.commit()
        flash(f"{gamename.gamename} delete successfully!")
        return redirect(url_for("hello"))