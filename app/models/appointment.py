from app.db import db
import uuid
from datetime import datetime

class Appointment(db.Model):
    __tablename__ = 'Appointments'

    appointment_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    date_time = db.Column(db.DateTime, nullable=False)
    appointment_type = db.Column(db.String, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    physio_id = db.Column(db.String, db.ForeignKey('Physios.physio_id', ondelete='CASCADE'), nullable=False)
