import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.db import db
from app.models import Treatment

# Define the TreatmentType to expose the SQLAlchemy model via GraphQL
class TreatmentType(SQLAlchemyObjectType):
    class Meta:
        model = Treatment
        fields = ('treatment_id', 'treatment_name', 'description')


# Create Treatment Mutation
class CreateTreatment(graphene.Mutation):
    class Arguments:
        treatment_name = graphene.String(required=True)
        description = graphene.String(required=True)

    treatment = graphene.Field(TreatmentType)

    def mutate(self, info, treatment_name, description):
        treatment = Treatment(
            treatment_name=treatment_name,
            description=description
        )
        db.session.add(treatment)
        db.session.commit()
        return CreateTreatment(treatment=treatment)


# Update Treatment Mutation
class UpdateTreatment(graphene.Mutation):
    class Arguments:
        treatment_id = graphene.String(required=True)
        treatment_name = graphene.String()
        description = graphene.String()

    treatment = graphene.Field(TreatmentType)

    def mutate(self, info, treatment_id, treatment_name=None, description=None):
        treatment = Treatment.query.filter_by(treatment_id=treatment_id).first()
        if not treatment:
            raise Exception("Treatment not found")

        if treatment_name:
            treatment.treatment_name = treatment_name
        if description:
            treatment.description = description

        db.session.commit()
        return UpdateTreatment(treatment=treatment)


# Delete Treatment Mutation
class DeleteTreatment(graphene.Mutation):
    class Arguments:
        treatment_id = graphene.String(required=True)

    treatment_id = graphene.String()

    def mutate(self, info, treatment_id):
        treatment = Treatment.query.filter_by(treatment_id=treatment_id).first()
        if not treatment:
            raise Exception("Treatment not found")

        db.session.delete(treatment)
        db.session.commit()
        return DeleteTreatment(treatment_id=treatment_id)


# Query to fetch a specific Treatment by treatment_id
class Query(graphene.ObjectType):
    treatment = graphene.Field(TreatmentType, treatment_id=graphene.String(required=True))
    treatments = graphene.List(TreatmentType)

    def resolve_treatment(self, info, treatment_id):
        return Treatment.query.filter_by(treatment_id=treatment_id).first()

    def resolve_treatments(self, info):
        return Treatment.query.all()


# Root Mutation to define CRUD operations
class Mutation(graphene.ObjectType):
    create_treatment = CreateTreatment.Field()
    update_treatment = UpdateTreatment.Field()
    delete_treatment = DeleteTreatment.Field()


# Define the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
