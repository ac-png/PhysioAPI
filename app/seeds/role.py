from app.db import db
from app.models import Role
import uuid

def seed_roles():
    db.session.query(Role).delete()
    db.session.commit()

    public_role = Role(role_id=str(uuid.uuid4()), role_name='Public')
    client_role = Role(role_id=str(uuid.uuid4()), role_name='Client')
    staff_role = Role(role_id=str(uuid.uuid4()), role_name='Staff')

    db.session.add(public_role)
    db.session.add(client_role)
    db.session.add(staff_role)

    db.session.commit()

    print("Roles have been seeded successfully!")

if __name__ == "__main__":
    seed_roles()
