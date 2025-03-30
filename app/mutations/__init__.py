# Importing authentication-related mutations
from .auth import RegisterMutation, LoginMutation, LogoutMutation

# Importing program-related mutations and types
from .program import CreateProgram, UpdateProgram, DeleteProgram, ProgramType

# Importing physio-related mutations and types
from .details import CreatePhysio, UpdatePhysio, DeletePhysio, PhysioType

# Importing patient-related mutations and types
from .details import CreatePatient, UpdatePatient, DeletePatient, PatientType

# Importing appointment-related mutations and types
from .appointment import CreateAppointment, UpdateAppointment, DeleteAppointment, AppointmentType

# Importing exercise-related mutations and types
from .exercise import CreateExercise, UpdateExercise, DeleteExercise, ExerciseType

# Importing treatment-related mutations and types
from .treatment import CreateTreatment, UpdateTreatment, DeleteTreatment, TreatmentType