from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models.games import Games
from app.gamebrary import db, server
from helpers.helpers import GameForm
import os
import time


class GameController:
    def hello():
        gamelist = Games.query.order_by(Games.id)   
        return render_template('game/gamelist.html', page_title='Gamebrary', header_title="Games", games=gamelist)
        
    
    def new():
        if 'logged_user' not in session or session['logged_user'] == None:
            return redirect(url_for("login", next=url_for("new")))
        game_form = GameForm()
        return render_template("create/new_game.html", title="Register your game", page_title='Gamebrary', form_game=game_form)


    def create():
        game_form = GameForm(request.form)
        
        if not game_form.validate_on_submit():
            return Exception("Your form is not valid!"), redirect(url_for("hello"))

        name = game_form.name.data
        category = game_form.category.data
        console = game_form.console.data
        
        game = Games.query.filter_by(gamename=name).first()
        
        if game:
            flash("This Game already exists!")
            return redirect(url_for("hello"))
        
        new_game = Games(gamename=name, category=category, console=console)
        
        db.session.add(new_game)
        db.session.commit()
        
        file = request.files['filename']
        upload_path = server.config['UPLOAD_PATH']
        timestamp = time.time()
        file.save(f'{upload_path}/cover-{new_game.id}-{new_game.gamename}-{timestamp}.jpg')
        
        return redirect(url_for("hello")) 

    
    def image_cover(coverfile):
        return send_from_directory(os.path.join("..", "uploads"), coverfile)
