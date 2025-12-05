from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    animal_name = Column(String(100), nullable=False)
    gender = Column(String(1), nullable=False)

    # relationship
    sightings = relationship("Sighting", back_populates="animal")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    # relationship
    sightings = relationship("Sighting", back_populates="user")


class Sighting(Base):
    __tablename__ = "sightings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False)
    description = Column(String(255), nullable=False)
    location = Column(String(100), nullable=False)
    age_estimate = Column(Integer, nullable=False)

    # relationships
    user = relationship("User", back_populates="sightings")
    animal = relationship("Animal", back_populates="sightings")
    feedback = relationship("Feedback", back_populates="sighting", cascade="all, delete-orphan")


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    sighting_id = Column(Integer, ForeignKey("sightings.id"), nullable=False)
    message = Column(String(100), nullable=False)

    # relationship
    sighting = relationship("Sighting", back_populates="feedback")
