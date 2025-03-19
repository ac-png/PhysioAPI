from app.db import db
from datetime import datetime
import uuid

class Feedback(db.Model):
    __tablename__ = 'Feedback'

    feedback_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    pain_level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
