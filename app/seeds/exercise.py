from app.db import db
from app.models import Exercise
from faker import Faker
import uuid

fake = Faker()

def create_exercise(treatment_id):
    return Exercise(
        exercise_id=str(uuid.uuid4()),
        exercise_name=fake.word(),
        equipment=fake.word(),
        instructions=fake.sentence(),
        video_link=fake.url(),
        muscles_worked=fake.word(),
        benefits=fake.sentence(),
        image_link=fake.url(),
        treatment_id=treatment_id
    )

def seed_exercises(treatments):
    exercises = [create_exercise(treatments[i % len(treatments)].treatment_id) for i in range(10)]
    db.session.add_all(exercises)
    db.session.commit()
    print("Exercises seeded!")
