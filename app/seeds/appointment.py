from app.db import db
import uuid
from datetime import datetime
from app.models import Appointment, User, Physio
from faker import Faker

fake = Faker()

def seed_appointments():
    db.session.query(Appointment).delete()
    db.session.commit()

    users = db.session.query(User).all()
    physios = db.session.query(Physio).all()

    if len(users) < 3 or len(physios) < 3:
        print("Not enough users or physios to create appointments.")
        return

    appointment1 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Consultation",
        notes=fake.text(),
        user_id=users[0].user_id,
        physio_id=physios[0].physio_id
    )

    appointment2 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Follow-up",
        notes=fake.text(),
        user_id=users[0].user_id,
        physio_id=physios[1].physio_id
    )

    appointment3 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Consultation",
        notes=fake.text(),
        user_id=users[0].user_id,
        physio_id=physios[2].physio_id
    )

    appointment4 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Follow-up",
        notes=fake.text(),
        user_id=users[1].user_id,
        physio_id=physios[0].physio_id
    )

    appointment5 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Consultation",
        notes=fake.text(),
        user_id=users[1].user_id,
        physio_id=physios[1].physio_id
    )

    appointment6 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Follow-up",
        notes=fake.text(),
        user_id=users[1].user_id,
        physio_id=physios[2].physio_id
    )

    appointment7 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Consultation",
        notes=fake.text(),
        user_id=users[2].user_id,
        physio_id=physios[0].physio_id
    )

    appointment8 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Follow-up",
        notes=fake.text(),
        user_id=users[2].user_id,
        physio_id=physios[1].physio_id
    )

    appointment9 = Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_time(),
        appointment_type="Consultation",
        notes=fake.text(),
        user_id=users[2].user_id,
        physio_id=physios[2].physio_id
    )

    db.session.add(appointment1)
    db.session.add(appointment2)
    db.session.add(appointment3)
    db.session.add(appointment4)
    db.session.add(appointment5)
    db.session.add(appointment6)
    db.session.add(appointment7)
    db.session.add(appointment8)
    db.session.add(appointment9)

    db.session.commit()

    print("Appointments have been seeded successfully!")

if __name__ == "__main__":
    seed_appointments()
