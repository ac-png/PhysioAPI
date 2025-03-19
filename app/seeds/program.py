from app.db import db
from app.models import Program
from faker import Faker
import uuid
import random

fake = Faker()

def create_program(user_id, physio_id):
    return Program(
        program_id=str(uuid.uuid4()),
        program_name=fake.word(),
        start_date=fake.date_this_month(),
        num_days=random.randint(7, 30),
        user_id=user_id,
        physio_id=physio_id
    )

def seed_programs(users, physios):
    programs = []
    for user in users:
        program = create_program(user.user_id, physios[0].physio_id)  # You can adjust this logic as needed
        programs.append(program)
        db.session.add(program)
    db.session.commit()
    print("Programs seeded!")
