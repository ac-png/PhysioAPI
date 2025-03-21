from app.db import db
import uuid

class Treatment(db.Model):
    __tablename__ = 'Treatments'

    treatment_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    treatment_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    patient_id = db.Column(db.String, db.ForeignKey('Patients.patient_id', ondelete='CASCADE'), nullable=False)
