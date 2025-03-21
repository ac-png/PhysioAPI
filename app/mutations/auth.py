import graphene
import jwt
import datetime
import uuid
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app.db import db

class RegisterMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        roleId = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, email, password, roleId):
        if '@' not in email:
            return RegisterMutation(success=False, message="Invalid email format")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return RegisterMutation(success=False, message="Email already registered")

        new_user = User(
            user_id=str(uuid.uuid4()),
            email=email,
            password=generate_password_hash(password),
            role_id=roleId
        )

        db.session.add(new_user)
        db.session.commit()

        return RegisterMutation(success=True, message="User registered successfully")

class LoginMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    token = graphene.String()

    def mutate(self, info, email, password):
        if '@' not in email:
            return LoginMutation(success=False, token=None)

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            secret_key = current_app.config['SECRET_KEY']
            payload = {
                'user_id': user.user_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, secret_key, algorithm="HS256")
            return LoginMutation(success=True, token=token)

        return LoginMutation(success=False, token=None)

class LogoutMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, token):
        return LogoutMutation(success=True, message="Logged out successfully")
