from app.seeds import seed_physios, seed_feedback, seed_treatments, seed_users, seed_programs, seed_exercises, seed_appointments, seed_exercise_sessions
from app.models import Physio, User, Treatment, Exercise, Appointment, ExerciseSession

def seed_data():
    print("Seeding data...")

    physios = Physio.query.all()
    users = User.query.all()
    treatments = Treatment.query.all()
    exercises = Exercise.query.all()
    appointments = Appointment.query.all()
    exercise_sessions = ExerciseSession.query.all()

    seed_physios()
    seed_feedback()
    seed_treatments()
    seed_users(physios)
    seed_programs(users, physios)
    seed_exercises(treatments)
    seed_appointments(users, physios)
    seed_exercise_sessions(exercises, users)

    print("Seeding completed.")

def clear_old_data():
    print("Clearing old data...")
