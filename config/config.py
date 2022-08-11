import os

CONFIG = {
    "SECRET_KEY": os.getenv("SECRET_KEY", "secret_cookie"), 
    "SQLALCHEMY_DATABASE_URI": "{DMBS}://{db_user}:{db_pass}@{db_server}/{db_name}".format(
        DMBS = os.getenv("DMBS", "mysql+mysqlconnector"),
        db_user = os.getenv("DB_USER", "root"),
        db_pass = os.getenv("DB_PASS","python"),
        db_server = os.getenv("DB_SERVER","localhost"),
        db_name = os.getenv("DB_NAME","gamebrary"),
    ), 

}

UPLOAD_PATH = os.path.join("uploads/")