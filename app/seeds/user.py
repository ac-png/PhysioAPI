from app.db import db
from app.models import User, Role
import uuid
from faker import Faker

fake = Faker()

def seed_users():
    db.session.query(User).delete()
    db.session.commit()

    roles = db.session.query(Role).all()

    if len(roles) < 3:
        print("Not enough roles to create users.")
        return

    user1 = User(
        user_id=str(uuid.uuid4()),
        email=fake.email(),
        password='password123',
        role_id=roles[0].role_id
    )

    user2 = User(
        user_id=str(uuid.uuid4()),
        email=fake.email(),
        password='password123',
        role_id=roles[1].role_id
    )

    user3 = User(
        user_id=str(uuid.uuid4()),
        email=fake.email(),
        password='password123',
        role_id=roles[2].role_id
    )

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.commit()

    print("Users have been seeded successfully!")

if __name__ == "__main__":
    seed_users()
