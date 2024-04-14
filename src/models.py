from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(30), unique=False, nullable=False)
    last_name = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(40), unique=True, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    planet_id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(100))
    diameter = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    description = db.Column(db.String(400))
    favorites = db.relationship('Favorites', backref='planet', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.planet_id

    def serialize(self):
        return {
            "planet_id": self.planet_id,
            "planet_name": self.planet_name,
            "diameter": self.diameter,
            "temperature": self.temperature,
            "description": self.description
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(250))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    favorites = db.relationship('Favorites', backref='person', lazy=True)

    def __repr__(self):
        return '<People %r>' % self.person_id

    def serialize(self):
        return {
            "person_id": self.person_id,
            "person_name": self.person_name,
            "weight": self.weight,
            "height": self.height,
            # do not serialize the password, its a security breach
        }
    
class Favorites(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('people.person_id'), primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.planet_id'), primary_key=True)

    def __repr__(self):
        return '<Favorites %r>' % self.id