"""empty message

Revision ID: e304e393cb48
Revises: a5cffa318ac2
Create Date: 2024-04-12 01:03:11.544503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e304e393cb48'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(length=250), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('character_id')
    )
    op.create_table('planets',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=100), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('temperature', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.PrimaryKeyConstraint('planet_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('username', sa.String(length=40), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    op.drop_table('planets')
    op.drop_table('character')
    # ### end Alembic commands ###
