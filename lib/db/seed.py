from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Animal, Sighting, User, Feedback


DATABASE_URL = "sqlite:////home/abiud/Development/code/phase-3/Logify_db/lib/db/animals.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


# USER 

def create_user(username, email, password):
    db = SessionLocal()
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()


def get_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    print(users)


def update_user(id, username, email, password):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    if user:
        user.username = username
        user.email = email
        user.password = password
        db.commit()
    db.close()


def delete_user(id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
    db.close()


# animal

def create_animal(animal_name, gender):
    db = SessionLocal()
    animal = Animal(animal_name=animal_name, gender=gender)
    db.add(animal)
    db.commit()
    db.refresh(animal)
    db.close()


def get_all_animals():
    db = SessionLocal()
    animals = db.query(Animal).all()
    db.close()
    print(animals)


def update_animal(id, animal_name, gender):
    db = SessionLocal()
    animal = db.query(Animal).filter(Animal.id == id).first()
    if animal:
        animal.animal_name = animal_name
        animal.gender = gender
        db.commit()
    db.close()


def delete_animal(id):
    db = SessionLocal()
    animal = db.query(Animal).filter(Animal.id == id).first()
    if animal:
        db.delete(animal)
        db.commit()
    db.close()


# sighting

def create_sighting(user_id, animal_id, description, location, age_estimate):
    db = SessionLocal()
    sighting = Sighting(
        user_id=user_id,
        animal_id=animal_id,
        description=description,
        location=location,
        age_estimate=age_estimate
    )
    db.add(sighting)
    db.commit()
    db.refresh(sighting)
    db.close()


def get_all_sightings():
    db = SessionLocal()
    sightings = db.query(Sighting).all()
    db.close()
    print(sightings)


def update_sighting(id, user_id, animal_id, description, location, age_estimate):
    db = SessionLocal()
    sighting = db.query(Sighting).filter(Sighting.id == id).first()
    if sighting:
        sighting.user_id = user_id
        sighting.animal_id = animal_id
        sighting.description = description
        sighting.location = location
        sighting.age_estimate = age_estimate
        db.commit()
    db.close()


def delete_sighting(id):
    db = SessionLocal()
    sighting = db.query(Sighting).filter(Sighting.id == id).first()
    if sighting:
        db.delete(sighting)
        db.commit()
    db.close()


# feedback

def create_feedback(sighting_id, message):
    db = SessionLocal()
    feedback = Feedback(sighting_id=sighting_id, message=message)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    db.close()


def get_all_feedback():
    db = SessionLocal()
    feedback = db.query(Feedback).all()
    db.close()
    print(feedback)


def update_feedback(id, sighting_id, message):
    db = SessionLocal()
    fb = db.query(Feedback).filter(Feedback.id == id).first()
    if fb:
        fb.sighting_id = sighting_id
        fb.message = message
        db.commit()
    db.close()


def delete_feedback(id):
    db = SessionLocal()
    fb = db.query(Feedback).filter(Feedback.id == id).first()
    if fb:
        db.delete(fb)
        db.commit()
    db.close()


# seed data

if __name__ == "__main__":

    #  users 
    create_user(username="baks", email="baks@gmail.com", password="123")
    get_all_users()

    # animals
    create_animal(animal_name="Lion", gender="M")
    create_animal(animal_name="Elephant", gender="F")
    get_all_animals()

    # sightings
    create_sighting(
        user_id=1,
        animal_id=1,
        description="Saw a lion resting under a tree",
        location="Nairobi National Park",
        age_estimate=5
    )

    create_sighting(
        user_id=1,
        animal_id=2,
        description="Elephant walking near the river",
        location="Tsavo",
        age_estimate=12
    )
    get_all_sightings()

    # feedback
    create_feedback(sighting_id=1, message="Great sighting!")
    create_feedback(sighting_id=2, message="Amazing experience.")
    get_all_feedback()


