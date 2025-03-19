from app.db import db
from app.models import Physio
from faker import Faker
import uuid

fake = Faker()

def create_physio():
    return Physio(
        physio_id=str(uuid.uuid4()),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        location=fake.city()
    )

def seed_physios():
    physios = [create_physio() for _ in range(5)]
    db.session.add_all(physios)
    db.session.commit()
    print("Physios seeded!")
