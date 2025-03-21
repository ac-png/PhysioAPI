from app.db import db
import uuid

class Program(db.Model):
    __tablename__ = 'Programs'

    program_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    program_name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    number_of_days = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    patient_id = db.Column(db.String, db.ForeignKey('Patients.patient_id', ondelete='CASCADE'), nullable=False)
    physio_id = db.Column(db.String, db.ForeignKey('Physios.physio_id', ondelete='CASCADE'), nullable=False)
