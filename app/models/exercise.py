from app.db import db
import uuid

class Exercise(db.Model):
    __tablename__ = 'Exercises'

    exercise_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    exercise_name = db.Column(db.String(255), nullable=False)
    equipment = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.String(255), nullable=False)
    video_link = db.Column(db.String(255), nullable=False)
    muscles = db.Column(db.String(255), nullable=False)
    benefits = db.Column(db.String(255), nullable=False)
    image_link = db.Column(db.String(255), nullable=False)
    reps = db.Column(db.String(255), nullable=False)
    sets = db.Column(db.String(255), nullable=False)
    frequency = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    patient_id = db.Column(db.String, db.ForeignKey('Patients.patient_id', ondelete='CASCADE'), nullable=False)
    program_id = db.Column(db.String, db.ForeignKey('Programs.program_id', ondelete='CASCADE'), nullable=False)
    treatment_id = db.Column(db.String, db.ForeignKey('Treatments.treatment_id', ondelete='CASCADE'), nullable=False)
