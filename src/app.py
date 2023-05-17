"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Planets, Characters, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)

############################### GET ###############################

@app.route('/users', methods=['GET'])
def get_users():

    users = Users.query.all()

    user_list = [element.serialize() for element in users]
    return jsonify(user_list), 200


@app.route('/planets', methods=['GET'])
def get_planet():
    planets = Planets.query.all()

    planet_list = [element.serialize() for element in planets]
    return jsonify(planet_list), 200


@app.route('/characters', methods=['GET'])
def get_character():
    character = Characters.query.all()

    characters_list = [element.serialize() for element in character]
    return jsonify(characters_list), 200


@app.route('/favorite', methods=['GET'])
def get_favorite():
    favorite = Favorites.query.all()

    favorite_list = [element.serialize() for element in favorite]
    return jsonify(favorite_list), 200

############################### GET/ID #############################

@app.route('/users/<int:users_id>', methods=['GET'])
def get_user_id(users_id):
    user_id = Users.query.get(users_id)
    result = user_id.serialize()
    return jsonify(result), 200


@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planet_id(planets_id):
    planet_id = Planets.query.get(planets_id)
    result = planet_id.serialize()
    return jsonify(result), 200


@app.route('/characters/<int:characters_id>', methods=['GET'])
def get_character_id(characters_id):
    character_id = Characters.query.get(characters_id)
    result = character_id.serialize()
    return jsonify(result), 200

############################### POST ###############################

@app.route('/users', methods = ['POST'])
def create_user():
    data = request.get_json()
    user = Users(username = data['username'], email = data['email'], password = data['password'])
    db.session.add(user)
    db.session.commit()

    response_body = {'msg': 'User inserted successfully'}
    return jsonify({
        "response": response_body,
        "user": user.serialize()
    }), 200



@app.route('/planets', methods = ['POST'])
def create_planet():
    data = request.get_json()
    planet = Planets(name = data['name'], rotation_period = data['rotation_period'], orbital_period = data['orbital_period'],
                    diameter = data['diameter'], climate = data['climate'], terrain = data['terrain'],  population = data['population'])

    db.session.add(planet)
    db.session.commit()

    response_body = {"msg": "Planet inserted successfully"}
    return jsonify({
        "response": response_body,
        "planet": planet.serialize()
    }), 200
    
     
     
     
@app.route('/characters', methods = ['POST'])
def create_character(): 
    data = request.get_json()
    character = Characters (name = data['name'], heigth = data['heigth'], mass = data['mass'],
                    hair_color = data['hair_color'], eye_color = data['eye_color'], birth_year = data['birth_year'], gender = data['gender'])

    db.session.add(character)
    db.session.commit()

    response_body = {"msg": "Character inserted successfully"}
    return jsonify({
        "response": response_body,
        "character": character.serialize()
    }), 200



############################### DELETE #############################


@app.route('/users/<int:users_id>', methods = ['DELETE'])
def delete_user(users_id):
    user = Users.query.get(users_id)
    db.session.delete(user)
    db.session.commit()

    response_body = {"msg": "User deleted successfully"}
    return jsonify({
        "response": response_body,
        "character": user.serialize()
    }),200




@app.route('/characters/<int:characters_id>', methods = ['DELETE'])
def delete_character(characters_id):
    character = Characters.query.get(characters_id)
    db.session.delete(character)
    db.session.commit()

    response_body = {"msg": "Character deleted successfully"}
    return jsonify({
        "response": response_body,
        "character": character.serialize()
    }),200



@app.route('/planets/<int:planets_id>', methods = ['DELETE'])
def delete_planet(planets_id):
    planet = Planets.query.get(planets_id)
    db.session.delete(planet)
    db.session.commit()

    response_body = {"msg": "Planet deleted successfully"}
    return jsonify({
        "response": response_body,
        "character": planet.serialize()
    }),200

     

     # this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)



    #   {
    # "birth_year": "41.9BBY",
    # "eye_color": "white",
    # "gender": "male",
    # "hair_color": "none",
    # "heigth": 202.0,
    # "id": 2,
    # "mass": 136.0,
    # "name": "Darth Vader"
#   }


# {
#   "climate": "temperate",
#   "diameter": 118000,
#   "id": 4,
#   "name": "Bespin",
#   "orbital_period": 5110,
#   "population": 6000000.0,
#   "rotation_period": 12,
#   "terrain": "gas giant"
# }