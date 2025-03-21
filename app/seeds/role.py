from app.db import db
from app.models import Role
import uuid

def seed_roles():
    db.session.query(Role).delete()
    db.session.commit()

    patient_role = Role(role_id=str(uuid.uuid4()), role_name='Patient')
    physio_role = Role(role_id=str(uuid.uuid4()), role_name='Physio')

    db.session.add(patient_role)
    db.session.add(physio_role)

    db.session.commit()

    print("Roles have been seeded successfully!")

if __name__ == "__main__":
    seed_roles()
