"""empty message

Revision ID: 20d233414ba0
Revises: 16a571fb9cda
Create Date: 2023-05-18 11:44:38.142029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d233414ba0'
down_revision = '16a571fb9cda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('users_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('planets_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('characters_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('favorites_character_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorites_user_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorites_planet_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['users_id'], ['id'])
        batch_op.create_foreign_key(None, 'characters', ['characters_id'], ['id'])
        batch_op.create_foreign_key(None, 'planets', ['planets_id'], ['id'])
        batch_op.drop_column('character_id')
        batch_op.drop_column('planet_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('planet_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorites_planet_id_fkey', 'planets', ['planet_id'], ['id'])
        batch_op.create_foreign_key('favorites_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key('favorites_character_id_fkey', 'characters', ['character_id'], ['id'])
        batch_op.drop_column('characters_id')
        batch_op.drop_column('planets_id')
        batch_op.drop_column('users_id')

    # ### end Alembic commands ###
