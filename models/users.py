from app.gamebrary import db

class Users(db.Model):
    
    nick = db.Column(db.String(20), primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Name %r>" % self.name