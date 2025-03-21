from app.db import db
import uuid

class Patient(db.Model):
    __tablename__ = 'Patients'

    patient_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    condition = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)