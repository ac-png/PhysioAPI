from app.db import db
import uuid

class User(db.Model):
    __tablename__ = 'Users'

    user_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.String, db.ForeignKey('Roles.role_id', ondelete='CASCADE'), nullable=False)
