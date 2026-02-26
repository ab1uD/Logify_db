from flask import Flask, request, jsonify, abort
from backend.db import seed
from backend.db.models import User, Animal, Sighting, Feedback

app = Flask(__name__)

# helpers

def to_dict(obj):
    # simple serialization based on __dict__ but ignore _sa_instance_state
    data = {k: v for k, v in obj.__dict__.items() if not k.startswith('_sa_')}
    return data

# user endpoints

@app.route('/users', methods=['GET'])
def list_users():
    users = seed.get_all_users()
    return jsonify([to_dict(u) for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    required = ['username', 'email', 'password']
    if not all(key in data for key in required):
        abort(400)
    user = seed.create_user(data['username'], data['email'], data['password'])
    return jsonify(to_dict(user)), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json() or {}
    user = seed.update_user(user_id, data.get('username'), data.get('email'), data.get('password'))
    return ('', 204)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    seed.delete_user(user_id)
    return ('', 204)

# animals

@app.route('/animals', methods=['GET'])
def list_animals():
    animals = seed.get_all_animals()
    return jsonify([to_dict(a) for a in animals])

@app.route('/animals', methods=['POST'])
def create_animal():
    data = request.get_json() or {}
    if 'animal_name' not in data or 'gender' not in data:
        abort(400)
    animal = seed.create_animal(data['animal_name'], data['gender'])
    return jsonify(to_dict(animal)), 201

@app.route('/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    data = request.get_json() or {}
    seed.update_animal(animal_id, data.get('animal_name'), data.get('gender'))
    return ('', 204)

@app.route('/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    seed.delete_animal(animal_id)
    return ('', 204)

# sightings

@app.route('/sightings', methods=['GET'])
def list_sightings():
    sightings = seed.get_all_sightings()
    return jsonify([to_dict(s) for s in sightings])

@app.route('/sightings', methods=['POST'])
def create_sighting():
    data = request.get_json() or {}
    required = ['user_id', 'animal_id', 'description', 'location', 'age_estimate']
    if not all(key in data for key in required):
        abort(400)
    sighting = seed.create_sighting(data['user_id'], data['animal_id'], data['description'], data['location'], data['age_estimate'])
    return jsonify(to_dict(sighting)), 201

@app.route('/sightings/<int:sighting_id>', methods=['PUT'])
def update_sighting(sighting_id):
    data = request.get_json() or {}
    seed.update_sighting(sighting_id, data.get('user_id'), data.get('animal_id'), data.get('description'), data.get('location'), data.get('age_estimate'))
    return ('', 204)

@app.route('/sightings/<int:sighting_id>', methods=['DELETE'])
def delete_sighting(sighting_id):
    seed.delete_sighting(sighting_id)
    return ('', 204)

# feedback

@app.route('/feedback', methods=['GET'])
def list_feedback():
    feedback = seed.get_all_feedback()
    return jsonify([to_dict(fb) for fb in feedback])

@app.route('/feedback', methods=['POST'])
def create_feedback():
    data = request.get_json() or {}
    if 'sighting_id' not in data or 'message' not in data:
        abort(400)
    fb = seed.create_feedback(data['sighting_id'], data['message'])
    return jsonify(to_dict(fb)), 201

@app.route('/feedback/<int:fb_id>', methods=['PUT'])
def update_feedback(fb_id):
    data = request.get_json() or {}
    seed.update_feedback(fb_id, data.get('sighting_id'), data.get('message'))
    return ('', 204)

@app.route('/feedback/<int:fb_id>', methods=['DELETE'])
def delete_feedback(fb_id):
    seed.delete_feedback(fb_id)
    return ('', 204)


if __name__ == '__main__':
    # ensure database and tables exist
    from backend.db.models import Base
    Base.metadata.create_all(seed.engine)
    app.run(debug=True)
