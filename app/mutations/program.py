import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.db import db
from app.models import Program


# Define the ProgramType to expose the SQLAlchemy model via GraphQL
class ProgramType(SQLAlchemyObjectType):
    class Meta:
        model = Program
        fields = ('program_id', 'program_name', 'start_date', 'number_of_days', 'description', 'patient_id', 'physio_id')


# Mutation to create a Program
class CreateProgram(graphene.Mutation):
    class Arguments:
        program_name = graphene.String(required=True)
        start_date = graphene.DateTime(required=True)
        number_of_days = graphene.Int(required=True)
        description = graphene.String(required=True)
        patient_id = graphene.String(required=True)
        physio_id = graphene.String(required=True)

    program = graphene.Field(ProgramType)

    def mutate(self, info, program_name, start_date, number_of_days, description, patient_id, physio_id):
        program = Program(
            program_name=program_name,
            start_date=start_date,
            number_of_days=number_of_days,
            description=description,
            patient_id=patient_id,
            physio_id=physio_id
        )
        db.session.add(program)
        db.session.commit()
        return CreateProgram(program=program)


# Mutation to update a Program
class UpdateProgram(graphene.Mutation):
    class Arguments:
        program_id = graphene.String(required=True)
        program_name = graphene.String()
        start_date = graphene.DateTime()
        number_of_days = graphene.Int()
        description = graphene.String()
        patient_id = graphene.String()
        physio_id = graphene.String()

    program = graphene.Field(ProgramType)

    def mutate(self, info, program_id, program_name=None, start_date=None, number_of_days=None, description=None, patient_id=None, physio_id=None):
        program = Program.query.filter_by(program_id=program_id).first()
        if not program:
            raise Exception("Program not found")

        if program_name:
            program.program_name = program_name
        if start_date:
            program.start_date = start_date
        if number_of_days:
            program.number_of_days = number_of_days
        if description:
            program.description = description
        if patient_id:
            program.patient_id = patient_id
        if physio_id:
            program.physio_id = physio_id

        db.session.commit()
        return UpdateProgram(program=program)


# Mutation to delete a Program
class DeleteProgram(graphene.Mutation):
    class Arguments:
        program_id = graphene.String(required=True)

    program_id = graphene.String()

    def mutate(self, info, program_id):
        program = Program.query.filter_by(program_id=program_id).first()
        if not program:
            raise Exception("Program not found")

        db.session.delete(program)
        db.session.commit()
        return DeleteProgram(program_id=program_id)


# Query to fetch a specific Program by program_id
class Query(graphene.ObjectType):
    # Fetch a specific Program
    program = graphene.Field(ProgramType, program_id=graphene.String(required=True))

    # Fetch all Programs
    programs = graphene.List(ProgramType)

    def resolve_program(self, info, program_id):
        return Program.query.filter_by(program_id=program_id).first()

    def resolve_programs(self, info):
        return Program.query.all()


# Root Mutation to define CRUD operations
class Mutation(graphene.ObjectType):
    create_program = CreateProgram.Field()
    update_program = UpdateProgram.Field()
    delete_program = DeleteProgram.Field()


# Define the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
