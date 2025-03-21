"""Initial Migration

Revision ID: c41ab5d68468
Revises: 
Create Date: 2025-03-21 10:13:34.162697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c41ab5d68468'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Roles',
    sa.Column('role_id', sa.String(), nullable=False),
    sa.Column('role_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('Users',
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['Roles.role_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('Patients',
    sa.Column('patient_id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('condition', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('patient_id')
    )
    op.create_table('Physios',
    sa.Column('physio_id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('company_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('specialisation', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('physio_id')
    )
    op.create_table('Appointments',
    sa.Column('appointment_id', sa.String(), nullable=False),
    sa.Column('patient_id', sa.String(), nullable=False),
    sa.Column('physio_id', sa.String(), nullable=False),
    sa.Column('appointment_date', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('appointment_type', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['Patients.patient_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['physio_id'], ['Physios.physio_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('appointment_id')
    )
    op.create_table('Programs',
    sa.Column('program_id', sa.String(), nullable=False),
    sa.Column('program_name', sa.String(length=255), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('number_of_days', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('patient_id', sa.String(), nullable=False),
    sa.Column('physio_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['Patients.patient_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['physio_id'], ['Physios.physio_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('program_id')
    )
    op.create_table('Treatments',
    sa.Column('treatment_id', sa.String(), nullable=False),
    sa.Column('treatment_name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('patient_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['Patients.patient_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('treatment_id')
    )
    op.create_table('Exercises',
    sa.Column('exercise_id', sa.String(), nullable=False),
    sa.Column('exercise_name', sa.String(length=255), nullable=False),
    sa.Column('equipment', sa.String(length=255), nullable=False),
    sa.Column('instructions', sa.String(length=255), nullable=False),
    sa.Column('video_link', sa.String(length=255), nullable=False),
    sa.Column('muscles', sa.String(length=255), nullable=False),
    sa.Column('benefits', sa.String(length=255), nullable=False),
    sa.Column('image_link', sa.String(length=255), nullable=False),
    sa.Column('reps', sa.String(length=255), nullable=False),
    sa.Column('sets', sa.String(length=255), nullable=False),
    sa.Column('frequency', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('patient_id', sa.String(), nullable=False),
    sa.Column('program_id', sa.String(), nullable=False),
    sa.Column('treatment_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['Patients.patient_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['program_id'], ['Programs.program_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['treatment_id'], ['Treatments.treatment_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('exercise_id')
    )
    op.create_table('Feedbacks',
    sa.Column('feedback_id', sa.String(), nullable=False),
    sa.Column('pain_level', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('exercise_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['exercise_id'], ['Exercises.exercise_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('feedback_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Feedbacks')
    op.drop_table('Exercises')
    op.drop_table('Treatments')
    op.drop_table('Programs')
    op.drop_table('Appointments')
    op.drop_table('Physios')
    op.drop_table('Patients')
    op.drop_table('Users')
    op.drop_table('Roles')
    # ### end Alembic commands ###
