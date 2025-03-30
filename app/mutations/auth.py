import graphene
import jwt
import datetime
import uuid
import re
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app.db import db
from app.models.role import Role  # Assuming roles are stored in a separate table


# Function to validate email using regex pattern
def is_valid_email(email):
    # Regex pattern for a valid email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# RegisterMutation: Handles user registration
class RegisterMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)  # User's email
        password = graphene.String(required=True)  # User's password
        roleId = graphene.String(required=True)  # User's role ID

    success = graphene.Boolean()  # Whether registration was successful
    message = graphene.String()  # Message for the result

    def mutate(self, info, email, password, roleId):
        # Validate email format
        if not is_valid_email(email):
            return RegisterMutation(success=False, message="Invalid email format")

        # Check if roleId exists in the database (i.e., valid role)
        role = Role.query.filter_by(role_id=roleId).first()
        if not role:
            return RegisterMutation(success=False, message="Invalid role ID")

        # Check if the email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return RegisterMutation(success=False, message="Email already registered")

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        # Create a new user object
        new_user = User(
            user_id=str(uuid.uuid4()),  # Unique user ID
            email=email,
            password=hashed_password,  # Hashed password
            role_id=roleId  # Role ID of the user
        )

        # Save the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return RegisterMutation(success=True, message="User registered successfully")


# LoginMutation: Handles user login and token generation
class LoginMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)  # User's email
        password = graphene.String(required=True)  # User's password

    success = graphene.Boolean()  # Whether login was successful
    token = graphene.String()  # JWT token for the authenticated user

    def mutate(self, info, email, password):
        # Validate email format
        if not is_valid_email(email):
            return LoginMutation(success=False, token=None)

        # Check if the user exists with the provided email
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):  # Validate password
            secret_key = current_app.config['SECRET_KEY']  # Get secret key for JWT

            # Create a payload with user ID and expiration time (1 hour)
            payload = {
                'user_id': user.user_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }

            # Generate a JWT token
            token = jwt.encode(payload, secret_key, algorithm="HS256")
            return LoginMutation(success=True, token=token)

        # If user not found or password incorrect
        return LoginMutation(success=False, token=None)


# LogoutMutation: Handles user logout
class LogoutMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)  # JWT token provided by user

    success = graphene.Boolean()  # Whether logout was successful
    message = graphene.String()  # Message after logging out

    def mutate(self, info, token):
        # In this basic case, we just assume the user logs out by discarding the token client-side.
        return LogoutMutation(success=True, message="Logged out successfully")


# RefreshTokenMutation: Allows refreshing of expired tokens
class RefreshTokenMutation(graphene.Mutation):
    class Arguments:
        refresh_token = graphene.String(required=True)  # Expired token to refresh

    success = graphene.Boolean()  # Whether token refresh was successful
    token = graphene.String()  # New refreshed token

    def mutate(self, info, refresh_token):
        try:
            secret_key = current_app.config['SECRET_KEY']  # Get secret key for JWT
            # Decode the refresh token to get payload
            payload = jwt.decode(refresh_token, secret_key, algorithms=["HS256"])

            # Check if the token has expired
            if datetime.datetime.utcfromtimestamp(payload['exp']) < datetime.datetime.utcnow():
                return RefreshTokenMutation(success=False, token=None)

            # If valid, create a new token with an updated expiration time
            new_payload = {
                'user_id': payload['user_id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            new_token = jwt.encode(new_payload, secret_key, algorithm="HS256")
            return RefreshTokenMutation(success=True, token=new_token)

        except jwt.ExpiredSignatureError:
            # Token has expired, return failure
            return RefreshTokenMutation(success=False, token=None)
        except jwt.InvalidTokenError:
            # Invalid token error, return failure
            return RefreshTokenMutation(success=False, token=None)
