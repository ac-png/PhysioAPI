from app.seeds import seed_physios, seed_roles, seed_users, seed_programs, seed_appointments

def seed_data():
    print("Seeding data...")
    seed_physios()
    seed_roles()
    seed_users()
    seed_programs()
    seed_appointments()
    print("Seeding completed.")

def clear_old_data():
    print("Clearing old data...")
