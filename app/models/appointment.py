from app.db import db
import uuid


class Appointment(db.Model):
    __tablename__ = 'Appointments'

    appointment_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    patient_id = db.Column(db.String, db.ForeignKey('Patients.patient_id', ondelete='CASCADE'), nullable=False)
    physio_id = db.Column(db.String, db.ForeignKey('Physios.physio_id', ondelete='CASCADE'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(255), nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    appointment_type = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.String(255), nullable=True)
