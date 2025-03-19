from app.db import db
from app.models import Feedback
from faker import Faker
import random
import uuid

fake = Faker()

def create_feedback():
    return Feedback(
        feedback_id=str(uuid.uuid4()),
        pain_level=random.randint(1, 10),
        description=fake.sentence(),
        date_time=fake.date_this_year()
    )

def seed_feedback():
    feedbacks = [create_feedback() for _ in range(10)]
    db.session.add_all(feedbacks)
    db.session.commit()
    print("Feedbacks seeded!")
