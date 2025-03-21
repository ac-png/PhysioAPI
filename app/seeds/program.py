from app.db import db
from app.models import Program, User, Physio
import uuid
from faker import Faker

fake = Faker()

def seed_programs():
    db.session.query(Program).delete()
    db.session.commit()

    users = db.session.query(User).all()
    physios = db.session.query(Physio).all()

    if len(users) < 3 or len(physios) < 3:
        print("Not enough users or physios to create programs.")
        return

    program1 = Program(
        program_id=str(uuid.uuid4()),
        program_name='Post-Surgery Knee Rehabilitation',
        start_date=fake.date_time(),
        num_days=fake.random_int(0,90),
        user_id=users[0].user_id,
        physio_id=physios[0].physio_id
    )

    program2 = Program(
        program_id=str(uuid.uuid4()),
        program_name='Chronic Lower Back Pain Relief',
        start_date=fake.date_time(),
        num_days=fake.random_int(0,90),
        user_id=users[1].user_id,
        physio_id=physios[1].physio_id
    )

    program3 = Program(
        program_id=str(uuid.uuid4()),
        program_name='Sports Injury Recovery: Shoulder',
        start_date=fake.date_time(),
        num_days=fake.random_int(0,90),
        user_id=users[2].user_id,
        physio_id=physios[2].physio_id
    )

    db.session.add(program1)
    db.session.add(program2)
    db.session.add(program3)

    db.session.commit()

    print("Programs have been seeded successfully!")

if __name__ == "__main__":
    seed_programs()
