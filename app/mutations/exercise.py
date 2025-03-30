import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.db import db
from app.models import Exercise


# Define the ExerciseType to expose the SQLAlchemy model via GraphQL
class ExerciseType(SQLAlchemyObjectType):
    class Meta:
        model = Exercise
        fields = ('exercise_id', 'exercise_name', 'equipment', 'instructions', 'video_link', 'muscles', 'benefits',
                  'image_link', 'reps', 'sets', 'frequency', 'status', 'patient_id', 'program_id', 'treatment_id')


# Mutation to create an Exercise
class CreateExercise(graphene.Mutation):
    class Arguments:
        exercise_name = graphene.String(required=True)
        equipment = graphene.String(required=True)
        instructions = graphene.String(required=True)
        video_link = graphene.String(required=True)
        muscles = graphene.String(required=True)
        benefits = graphene.String(required=True)
        image_link = graphene.String(required=True)
        reps = graphene.String(required=True)
        sets = graphene.String(required=True)
        frequency = graphene.String(required=True)
        status = graphene.String(required=True)
        patient_id = graphene.String(required=True)
        program_id = graphene.String(required=True)
        treatment_id = graphene.String(required=True)

    exercise = graphene.Field(ExerciseType)

    def mutate(self, info, exercise_name, equipment, instructions, video_link, muscles, benefits, image_link,
               reps, sets, frequency, status, patient_id, program_id, treatment_id):
        exercise = Exercise(
            exercise_name=exercise_name,
            equipment=equipment,
            instructions=instructions,
            video_link=video_link,
            muscles=muscles,
            benefits=benefits,
            image_link=image_link,
            reps=reps,
            sets=sets,
            frequency=frequency,
            status=status,
            patient_id=patient_id,
            program_id=program_id,
            treatment_id=treatment_id
        )
        db.session.add(exercise)
        db.session.commit()
        return CreateExercise(exercise=exercise)


# Mutation to update an Exercise
class UpdateExercise(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.String(required=True)
        exercise_name = graphene.String()
        equipment = graphene.String()
        instructions = graphene.String()
        video_link = graphene.String()
        muscles = graphene.String()
        benefits = graphene.String()
        image_link = graphene.String()
        reps = graphene.String()
        sets = graphene.String()
        frequency = graphene.String()
        status = graphene.String()
        patient_id = graphene.String()
        program_id = graphene.String()
        treatment_id = graphene.String()

    exercise = graphene.Field(ExerciseType)

    def mutate(self, info, exercise_id, exercise_name=None, equipment=None, instructions=None, video_link=None,
               muscles=None, benefits=None, image_link=None, reps=None, sets=None, frequency=None, status=None,
               patient_id=None, program_id=None, treatment_id=None):
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        if not exercise:
            raise Exception("Exercise not found")

        if exercise_name:
            exercise.exercise_name = exercise_name
        if equipment:
            exercise.equipment = equipment
        if instructions:
            exercise.instructions = instructions
        if video_link:
            exercise.video_link = video_link
        if muscles:
            exercise.muscles = muscles
        if benefits:
            exercise.benefits = benefits
        if image_link:
            exercise.image_link = image_link
        if reps:
            exercise.reps = reps
        if sets:
            exercise.sets = sets
        if frequency:
            exercise.frequency = frequency
        if status:
            exercise.status = status
        if patient_id:
            exercise.patient_id = patient_id
        if program_id:
            exercise.program_id = program_id
        if treatment_id:
            exercise.treatment_id = treatment_id

        db.session.commit()
        return UpdateExercise(exercise=exercise)


# Mutation to delete an Exercise
class DeleteExercise(graphene.Mutation):
    class Arguments:
        exercise_id = graphene.String(required=True)

    exercise_id = graphene.String()

    def mutate(self, info, exercise_id):
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        if not exercise:
            raise Exception("Exercise not found")

        db.session.delete(exercise)
        db.session.commit()
        return DeleteExercise(exercise_id=exercise_id)


# Query to fetch a specific Exercise by exercise_id
class Query(graphene.ObjectType):
    # Fetch a specific Exercise
    exercise = graphene.Field(ExerciseType, exercise_id=graphene.String(required=True))

    # Fetch all Exercises
    exercises = graphene.List(ExerciseType)

    def resolve_exercise(self, info, exercise_id):
        return Exercise.query.filter_by(exercise_id=exercise_id).first()

    def resolve_exercises(self, info):
        return Exercise.query.all()


# Root Mutation to define CRUD operations
class Mutation(graphene.ObjectType):
    create_exercise = CreateExercise.Field()
    update_exercise = UpdateExercise.Field()
    delete_exercise = DeleteExercise.Field()
