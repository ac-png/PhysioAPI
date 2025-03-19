from app.db import db
from app.models import ExerciseSession
from faker import Faker
import uuid
import random

fake = Faker()

def create_exercise_session(exercise_id, user_id, program_id):
    return ExerciseSession(
        exercise_session_id=str(uuid.uuid4()),
        exercise_id=exercise_id,
        user_id=user_id,
        program_id=program_id,
        date_time=fake.date_this_year(),
        duration=random.randint(20, 60),
        repetitions=random.randint(5, 20),
        sets=random.randint(1, 5)
    )

def seed_exercise_sessions(exercises, users, programs):
    exercise_sessions = []
    for exercise in exercises:
        for user in users:
            for program in programs:
                session = create_exercise_session(exercise.exercise_id, user.user_id, program.program_id)
                exercise_sessions.append(session)
                db.session.add(session)
    db.session.commit()
    print("Exercise sessions seeded!")
