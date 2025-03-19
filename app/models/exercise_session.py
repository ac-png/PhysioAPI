from app.db import db
import uuid

class ExerciseSession(db.Model):
    __tablename__ = 'ExerciseSessions'

    exercise_session_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    exercise_id = db.Column(db.String(36), db.ForeignKey('Exercises.exercise_id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('Users.user_id'), nullable=False)
    program_id = db.Column(db.String(36), db.ForeignKey('Programs.program_id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
