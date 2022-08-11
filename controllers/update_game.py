from flask import render_template, request, redirect, session, url_for
from models.games import Games
from app.gamebrary import db, server
from helpers.helpers import recover_img, delete_img, GameForm
import time


class UpdateGameController:

    def edit_game(id):
        if 'logged_user' not in session or session['logged_user'] == None:
            return redirect(url_for("login", next=url_for("edit_game", id=id)))
        consult_id = Games.query.filter_by(id=id).first()
        game_form = GameForm()
        game_form.name.data = consult_id.gamename
        game_form.category.data = consult_id.category
        game_form.console.data = consult_id.console
        new_img = recover_img(id)#game=consult_id
        return render_template("edit_game/edit_game.html", title="Edit game", page_title="Editing", id=id, new_img=new_img, form_game=game_form)


    def update_game():
        game_form = GameForm(request.form)
        
        consulted_game = Games.query.filter_by(id=request.form["id"]).first()

        consulted_game.gamename = game_form.name.data
        consulted_game.category = game_form.category.data
        consulted_game.console = game_form.console.data
        
        db.session.add(consulted_game)
        db.session.commit()
        
        file = request.files['filename']
        upload_path = server.config['UPLOAD_PATH']
        timestamp = time.time()
        delete_img(consulted_game.id)
        file.save(f'{upload_path}/cover-{consulted_game.id}-{consulted_game.gamename}-{timestamp}.jpg')

        return redirect(url_for("hello"))
