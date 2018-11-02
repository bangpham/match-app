from app import db

class User(db.model):
    __tablename__ = 'users'

    user_id = db.Column(db.Interger)
    email = db.Column(db.String())
    first = db.Column(db.String())
    last = db.Column(db.String())

    def __init__(self, email, first, last):
        self.email = email
        self.first = first
        self.last = last
    
    def __repr__(self):
        return '<email {}>'.format(self.email)