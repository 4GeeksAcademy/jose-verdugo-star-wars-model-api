from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
   

    def __repr__(self):
        return '<Users %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            'username' : self.username,
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(80), nullable=False)    
    terrain = db.Column(db.String(80), nullable=False)    
    population =  db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            'name' : self.name,
            "rotation_period": self.rotation_period,
            "orbital_period" : self.orbital_period,
            "diameter" : self.diameter,
            "climate" : self.climate,
            "terrain" : self.terrain,
            "population" : self.population
        }
    


class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    heigth = db.Column(db.Float, nullable=False)
    mass = db.Column(db.Float, nullable=False)
    hair_color = db.Column(db.String(80), nullable=False)
    eye_color = db.Column(db.String(80), nullable=False)
    birth_year = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name
    
    def serialize(self):
        return{
             "id": self.id,
            'name' : self.name,
            'heigth' : self.heigth,
            'mass' : self.mass,
            'hair_color' : self.hair_color,
            'eye_color' : self.eye_color,
            'birth_year' : self.birth_year,
            'gender' : self.gender,
        }
    

class FavoritePlanet (db.Model):
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, primary_key=True)
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=False, primary_key=True)

    user = db.relationship('Users', backref = 'favorites_planet')
    planet = db.relationship('Planets', backref = 'favorites_planet')
    

    def __repr__(self):
        return f'<FavoritePlanet {self.user.username}, {self.planet.name}>' 

class FavoriteCharacter (db.Model):
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, primary_key=True)
    characters_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False, primary_key=True)
    

    user = db.relationship('Users', backref = 'favorites_character')
    character = db.relationship('Characters', backref = 'favorites_character')

    def __repr__(self):
        return f'<FavoriteCharacter {self.user.username}, {self.character.name}>'


