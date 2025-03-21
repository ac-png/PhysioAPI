from app.seeds import seed_roles

def seed_data():
    print("Seeding data...")
    seed_roles()
    print("Seeding completed.")

def clear_old_data():
    print("Clearing old data...")
