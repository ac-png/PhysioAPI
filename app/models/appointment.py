from app.db import db
import uuid

class Appointment(db.Model):
    __tablename__ = 'Appointments'

    appointment_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    date_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    physio_id = db.Column(db.String, db.ForeignKey('Physios.physio_id', ondelete='CASCADE'), nullable=False)
