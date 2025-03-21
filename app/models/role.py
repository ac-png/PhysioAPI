from app.db import db
import uuid

class Role(db.Model):
    __tablename__ = 'Roles'

    role_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    role_name = db.Column(db.String(255), nullable=False)
