import __init__
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import CONFIG
import os
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt


server = Flask(
    __name__,
    template_folder=os.path.join("..", "views"), 
    static_folder=os.path.join("..", "static"),
)

server.config.from_mapping(CONFIG)
server.config.from_envvar('FLASK_CONFIG')

db = SQLAlchemy(server)
csrf = CSRFProtect(server)
bcrypt = Bcrypt(server)

from config.routes import *
 
if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80, debug=True)
