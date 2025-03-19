from app.db import db
import uuid

class Program(db.Model):
    __tablename__ = 'Programs'

    program_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    program_name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    num_days = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    physio_id = db.Column(db.String, db.ForeignKey('Physios.physio_id', ondelete='CASCADE'), nullable=False)
