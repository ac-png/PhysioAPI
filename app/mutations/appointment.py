import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.db import db
from app.models import Appointment

# Define the AppointmentType to expose the SQLAlchemy model via GraphQL
class AppointmentType(SQLAlchemyObjectType):
    class Meta:
        model = Appointment
        fields = (
            'appointment_id', 'patient_id', 'physio_id', 'appointment_date',
            'location', 'duration', 'appointment_type', 'status', 'notes'
        )


# Create Appointment Mutation
class CreateAppointment(graphene.Mutation):
    class Arguments:
        patient_id = graphene.String(required=True)
        physio_id = graphene.String(required=True)
        appointment_date = graphene.DateTime(required=True)
        location = graphene.String()
        duration = graphene.Int(required=True)
        appointment_type = graphene.String(required=True)
        status = graphene.String(required=True)
        notes = graphene.String()

    appointment = graphene.Field(AppointmentType)

    def mutate(self, info, patient_id, physio_id, appointment_date, location=None, duration=None, appointment_type=None, status=None, notes=None):
        appointment = Appointment(
            patient_id=patient_id,
            physio_id=physio_id,
            appointment_date=appointment_date,
            location=location,
            duration=duration,
            appointment_type=appointment_type,
            status=status,
            notes=notes
        )
        db.session.add(appointment)
        db.session.commit()
        return CreateAppointment(appointment=appointment)


# Update Appointment Mutation
class UpdateAppointment(graphene.Mutation):
    class Arguments:
        appointment_id = graphene.String(required=True)
        patient_id = graphene.String()
        physio_id = graphene.String()
        appointment_date = graphene.DateTime()
        location = graphene.String()
        duration = graphene.Int()
        appointment_type = graphene.String()
        status = graphene.String()
        notes = graphene.String()

    appointment = graphene.Field(AppointmentType)

    def mutate(self, info, appointment_id, patient_id=None, physio_id=None, appointment_date=None, location=None, duration=None, appointment_type=None, status=None, notes=None):
        appointment = Appointment.query.filter_by(appointment_id=appointment_id).first()
        if not appointment:
            raise Exception("Appointment not found")

        if patient_id:
            appointment.patient_id = patient_id
        if physio_id:
            appointment.physio_id = physio_id
        if appointment_date:
            appointment.appointment_date = appointment_date
        if location:
            appointment.location = location
        if duration:
            appointment.duration = duration
        if appointment_type:
            appointment.appointment_type = appointment_type
        if status:
            appointment.status = status
        if notes:
            appointment.notes = notes

        db.session.commit()
        return UpdateAppointment(appointment=appointment)


# Delete Appointment Mutation
class DeleteAppointment(graphene.Mutation):
    class Arguments:
        appointment_id = graphene.String(required=True)

    appointment_id = graphene.String()

    def mutate(self, info, appointment_id):
        appointment = Appointment.query.filter_by(appointment_id=appointment_id).first()
        if not appointment:
            raise Exception("Appointment not found")

        db.session.delete(appointment)
        db.session.commit()
        return DeleteAppointment(appointment_id=appointment_id)


# Query to fetch a specific Appointment by appointment_id
class Query(graphene.ObjectType):
    appointment = graphene.Field(AppointmentType, appointment_id=graphene.String(required=True))
    appointments = graphene.List(AppointmentType)

    def resolve_appointment(self, info, appointment_id):
        return Appointment.query.filter_by(appointment_id=appointment_id).first()

    def resolve_appointments(self, info):
        return Appointment.query.all()


# Root Mutation to define CRUD operations
class Mutation(graphene.ObjectType):
    create_appointment = CreateAppointment.Field()
    update_appointment = UpdateAppointment.Field()
    delete_appointment = DeleteAppointment.Field()


# Define the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
