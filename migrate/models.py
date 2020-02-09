from exts import db
class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    age=db.Column(db.Integer)