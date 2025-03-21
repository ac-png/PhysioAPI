from app.db import db
import uuid

class Feedback(db.Model):
    __tablename__ = 'Feedbacks'

    feedback_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    pain_level = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    exercise_id = db.Column(db.String, db.ForeignKey('Exercises.exercise_id', ondelete='CASCADE'), nullable=False)
