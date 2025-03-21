from app.db import db
import uuid

class Physio(db.Model):
    __tablename__ = 'Physios'

    physio_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
