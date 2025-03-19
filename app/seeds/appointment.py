from app.db import db
from app.models import Appointment
from faker import Faker
import uuid

fake = Faker()

def create_appointment(user_id, physio_id):
    return Appointment(
        appointment_id=str(uuid.uuid4()),
        date_time=fake.date_this_year(),
        user_id=user_id,
        physio_id=physio_id
    )

def seed_appointments(users, physios):
    appointments = []
    for user in users:
        appointment = create_appointment(user.user_id, physios[0].physio_id)  # Adjust logic as needed
        appointments.append(appointment)
        db.session.add(appointment)
    db.session.commit()
    print("Appointments seeded!")
