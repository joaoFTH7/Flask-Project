import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class GameForm(FlaskForm):
    name = StringField("Gamename", [validators.DataRequired(), validators.Length(min=1, max=50)])
    category = StringField("Category", [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField("Console", [validators.DataRequired(), validators.Length(min=1, max=20)])    
    input_save = SubmitField("Save")


class UserForm(FlaskForm):
    nick = StringField("Nickname", [validators.DataRequired(), validators.Length(min=1, max=20)])
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=1, max=100)])
    input_save = SubmitField("Enter")


def recover_img(id):
    for filename in os.listdir(os.path.join("uploads")):
        if f"cover-{id}" in filename:
            return filename
    
    return "capa_padrao.jpg"


def delete_img(id):
    file = recover_img(id)
    if file != "capa_padrao.jpg":
        os.remove(os.path.join("uploads", file))
      