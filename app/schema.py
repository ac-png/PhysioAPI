import graphene
# Importing authentication-related mutations
from app.mutations.auth import RegisterMutation, LoginMutation, LogoutMutation

# Importing program-related mutations
from app.mutations.program import CreateProgram, UpdateProgram, DeleteProgram, ProgramType

# Importing physio-related mutations
from app.mutations.details import CreatePhysio, UpdatePhysio, DeletePhysio, PhysioType

# Importing patient-related mutations
from app.mutations.details import CreatePatient, UpdatePatient, DeletePatient, PatientType

# Importing appointment-related mutations
from app.mutations.appointment import CreateAppointment, UpdateAppointment, DeleteAppointment, AppointmentType

# Importing exercise-related mutations
from app.mutations.exercise import CreateExercise, UpdateExercise, DeleteExercise, ExerciseType

# Importing treatment-related mutations
from app.mutations.treatment import CreateTreatment, UpdateTreatment, DeleteTreatment, TreatmentType

class Mutation(graphene.ObjectType):
    # Authentication mutations
    register = RegisterMutation.Field()
    login = LoginMutation.Field()
    logout = LogoutMutation.Field()

    # Program mutations
    create_program = CreateProgram.Field()
    update_program = UpdateProgram.Field()
    delete_program = DeleteProgram.Field()

    # Physio mutations
    create_physio = CreatePhysio.Field()
    update_physio = UpdatePhysio.Field()
    delete_physio = DeletePhysio.Field()

    # Patient mutations
    create_patient = CreatePatient.Field()
    update_patient = UpdatePatient.Field()
    delete_patient = DeletePatient.Field()

    # Appointment mutations
    create_appointment = CreateAppointment.Field()
    update_appointment = UpdateAppointment.Field()
    delete_appointment = DeleteAppointment.Field()

    # Exercise mutations
    create_exercise = CreateExercise.Field()
    update_exercise = UpdateExercise.Field()
    delete_exercise = DeleteExercise.Field()

    # Treatment mutations
    create_treatment = CreateTreatment.Field()
    update_treatment = UpdateTreatment.Field()
    delete_treatment = DeleteTreatment.Field()

# Defining the schema with mutations
schema = graphene.Schema(mutation=Mutation)
