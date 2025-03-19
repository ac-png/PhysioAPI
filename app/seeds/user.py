from app.db import db
from app.models import User
from werkzeug.security import generate_password_hash
from faker import Faker
import uuid

fake = Faker()

def create_user(physio_id):
    return User(
        user_id=str(uuid.uuid4()),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=generate_password_hash('password'),
        physio_id=physio_id
    )

def seed_users(physios):
    users = []
    for physio in physios:
        user = create_user(physio.physio_id)
        users.append(user)
        db.session.add(user)
    db.session.commit()
    print("Users seeded!")
    return users

