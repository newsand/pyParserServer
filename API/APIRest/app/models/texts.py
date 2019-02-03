from app import db
from app import manager

class Texts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    textname = db.Column(db.String(100))
    text = db.Column(db.String(100))

db.create_all()
manager.create_api(Texts, methods=['POST','GET','PUT','DELETE'])