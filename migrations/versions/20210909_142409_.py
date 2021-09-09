"""empty message

Revision ID: dd27492a3a1a
Revises: ffdc0a98111c
Create Date: 2021-09-09 14:24:09.787880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd27492a3a1a'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('children',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('profile_img_url', sa.Text(), nullable=True),
    sa.Column('allergies', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('arrival', sa.DateTime(), nullable=False),
    sa.Column('departure', sa.DateTime(), nullable=True),
    sa.Column('woke', sa.DateTime(), nullable=False),
    sa.Column('last_ate', sa.DateTime(), nullable=True),
    sa.Column('mood', sa.String(length=50), nullable=False),
    sa.Column('parent_comments', sa.Text(), nullable=True),
    sa.Column('teacher_comments', sa.Text(), nullable=True),
    sa.Column('needs_cd', sa.String(length=50), nullable=True),
    sa.Column('highlights', sa.Text(), nullable=True),
    sa.Column('child_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['child_id'], ['children.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bathroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('status_cd', sa.String(length=50), nullable=False),
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['report_id'], ['reports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feedings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('bottom', sa.Boolean(), nullable=True),
    sa.Column('ounces', sa.Integer(), nullable=True),
    sa.Column('amount', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['report_id'], ['reports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('naps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('status_cd', sa.String(length=50), nullable=False),
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['report_id'], ['reports.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('first_name', sa.String(length=40), nullable=False))
    op.add_column('users', sa.Column('last_name', sa.String(length=40), nullable=False))
    op.add_column('users', sa.Column('profile_img_url', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('role_cd', sa.String(length=10), nullable=True))
    op.add_column('users', sa.Column('school_id', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('class_id', sa.Integer(), nullable=False))
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_foreign_key(None, 'users', 'schools', ['school_id'], ['id'])
    op.create_foreign_key(None, 'users', 'classes', ['class_id'], ['id'])
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.drop_column('users', 'class_id')
    op.drop_column('users', 'school_id')
    op.drop_column('users', 'role_cd')
    op.drop_column('users', 'profile_img_url')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_table('naps')
    op.drop_table('feedings')
    op.drop_table('bathroom')
    op.drop_table('reports')
    op.drop_table('children')
    op.drop_table('schools')
    op.drop_table('classes')
    # ### end Alembic commands ###