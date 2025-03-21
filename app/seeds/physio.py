from app.db import db
from app.models import Physio
import uuid
from faker import Faker

fake = Faker()

def seed_physios():
    db.session.query(Physio).delete()
    db.session.commit()

    physio1 = Physio(
        physio_id=str(uuid.uuid4()),
        first_name='John',
        last_name='Doe',
        address=fake.address(),
        company_name=fake.company(),
        email='john.doe@example.com',
        phone=fake.phone_number(),
    )

    physio2 = Physio(
        physio_id=str(uuid.uuid4()),
        first_name='Jane',
        last_name='Smith',
        address = fake.address(),
        company_name = fake.company(),
        email = 'jane.smith@example.com',
        phone = fake.phone_number(),
    )

    physio3 = Physio(
        physio_id=str(uuid.uuid4()),
        first_name='Emily',
        last_name='Johnson',
        address=fake.address(),
        company_name=fake.company(),
        email='emily.johnson@example.com',
        phone=fake.phone_number(),
    )

    db.session.add(physio1)
    db.session.add(physio2)
    db.session.add(physio3)

    db.session.commit()

    print("Physio data has been seeded successfully!")

if __name__ == "__main__":
    seed_physios()
