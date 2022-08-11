import os
from flask import Flask, send_file
from flask import render_template, request, redirect, url_for, send_from_directory


app = Flask(__name__, template_folder=(os.path.join("..","templates")))



@app.route("/")
def manda_img():
    return render_template("/um-html.html")

@app.route("/otarota/<coverfile>")
def ota_img(coverfile):
    return send_from_directory(os.path.join("..", "templates"),coverfile)


app.run(host='0.0.0.0', debug=True)