import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.db import db
from app.models import Physio, Patient

# Physio GraphQL Type
class PhysioType(SQLAlchemyObjectType):
    class Meta:
        model = Physio
        fields = (
            'physio_id', 'first_name', 'last_name', 'address', 'company_name', 'email',
            'phone', 'specialisation', 'user_id'
        )

# Patient GraphQL Type
class PatientType(SQLAlchemyObjectType):
    class Meta:
        model = Patient
        fields = (
            'patient_id', 'first_name', 'last_name', 'address', 'date_of_birth', 'condition',
            'email', 'phone', 'user_id'
        )

# Create Physio Mutation
class CreatePhysio(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        address = graphene.String(required=True)
        company_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        specialisation = graphene.String(required=True)
        user_id = graphene.String(required=True)

    physio = graphene.Field(PhysioType)

    def mutate(self, info, first_name, last_name, address, company_name, email, phone, specialisation, user_id):
        physio = Physio(
            first_name=first_name,
            last_name=last_name,
            address=address,
            company_name=company_name,
            email=email,
            phone=phone,
            specialisation=specialisation,
            user_id=user_id
        )
        db.session.add(physio)
        db.session.commit()
        return CreatePhysio(physio=physio)

# Update Physio Mutation
class UpdatePhysio(graphene.Mutation):
    class Arguments:
        physio_id = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        address = graphene.String()
        company_name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        specialisation = graphene.String()
        user_id = graphene.String()

    physio = graphene.Field(PhysioType)

    def mutate(self, info, physio_id, first_name=None, last_name=None, address=None, company_name=None, email=None, phone=None, specialisation=None, user_id=None):
        physio = Physio.query.filter_by(physio_id=physio_id).first()
        if not physio:
            raise Exception("Physio not found")

        if first_name:
            physio.first_name = first_name
        if last_name:
            physio.last_name = last_name
        if address:
            physio.address = address
        if company_name:
            physio.company_name = company_name
        if email:
            physio.email = email
        if phone:
            physio.phone = phone
        if specialisation:
            physio.specialisation = specialisation
        if user_id:
            physio.user_id = user_id

        db.session.commit()
        return UpdatePhysio(physio=physio)

# Delete Physio Mutation
class DeletePhysio(graphene.Mutation):
    class Arguments:
        physio_id = graphene.String(required=True)

    physio_id = graphene.String()

    def mutate(self, info, physio_id):
        physio = Physio.query.filter_by(physio_id=physio_id).first()
        if not physio:
            raise Exception("Physio not found")

        db.session.delete(physio)
        db.session.commit()
        return DeletePhysio(physio_id=physio_id)

# Create Patient Mutation
class CreatePatient(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        address = graphene.String(required=True)
        date_of_birth = graphene.Date(required=True)
        condition = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        user_id = graphene.String(required=True)

    patient = graphene.Field(PatientType)

    def mutate(self, info, first_name, last_name, address, date_of_birth, condition, email, phone, user_id):
        patient = Patient(
            first_name=first_name,
            last_name=last_name,
            address=address,
            date_of_birth=date_of_birth,
            condition=condition,
            email=email,
            phone=phone,
            user_id=user_id
        )
        db.session.add(patient)
        db.session.commit()
        return CreatePatient(patient=patient)

# Update Patient Mutation
class UpdatePatient(graphene.Mutation):
    class Arguments:
        patient_id = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        address = graphene.String()
        date_of_birth = graphene.Date()
        condition = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        user_id = graphene.String()

    patient = graphene.Field(PatientType)

    def mutate(self, info, patient_id, first_name=None, last_name=None, address=None, date_of_birth=None, condition=None, email=None, phone=None, user_id=None):
        patient = Patient.query.filter_by(patient_id=patient_id).first()
        if not patient:
            raise Exception("Patient not found")

        if first_name:
            patient.first_name = first_name
        if last_name:
            patient.last_name = last_name
        if address:
            patient.address = address
        if date_of_birth:
            patient.date_of_birth = date_of_birth
        if condition:
            patient.condition = condition
        if email:
            patient.email = email
        if phone:
            patient.phone = phone
        if user_id:
            patient.user_id = user_id

        db.session.commit()
        return UpdatePatient(patient=patient)

# Delete Patient Mutation
class DeletePatient(graphene.Mutation):
    class Arguments:
        patient_id = graphene.String(required=True)

    patient_id = graphene.String()

    def mutate(self, info, patient_id):
        patient = Patient.query.filter_by(patient_id=patient_id).first()
        if not patient:
            raise Exception("Patient not found")

        db.session.delete(patient)
        db.session.commit()
        return DeletePatient(patient_id=patient_id)

# Root Mutation to handle all CRUD operations for Physio and Patient
class Mutation(graphene.ObjectType):
    create_physio = CreatePhysio.Field()
    update_physio = UpdatePhysio.Field()
    delete_physio = DeletePhysio.Field()
    create_patient = CreatePatient.Field()
    update_patient = UpdatePatient.Field()
    delete_patient = DeletePatient.Field()

# Root Query to handle fetching Physio and Patient
class Query(graphene.ObjectType):
    physio = graphene.Field(PhysioType, physio_id=graphene.String(required=True))
    patient = graphene.Field(PatientType, patient_id=graphene.String(required=True))

    def resolve_physio(self, info, physio_id):
        return Physio.query.filter_by(physio_id=physio_id).first()

    def resolve_patient(self, info, patient_id):
        return Patient.query.filter_by(patient_id=patient_id).first()

# Schema definition
schema = graphene.Schema(query=Query, mutation=Mutation)
