from app.db import db
from app.models import Treatment
from faker import Faker
import uuid

fake = Faker()

def create_treatment():
    return Treatment(
        treatment_id=str(uuid.uuid4()),
        treatment_name=fake.word(),
        description=fake.sentence()
    )

def seed_treatments():
    treatments = [create_treatment() for _ in range(10)]
    db.session.add_all(treatments)
    db.session.commit()
    print("Treatments seeded!")
