"""first models

Revision ID: 19696de9d819
Revises: 
Create Date: 2023-03-14 17:07:30.114780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19696de9d819'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_Category_id'), 'Category', ['id'], unique=False)
    op.create_table('Genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_Genre_id'), 'Genre', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Genre_id'), table_name='Genre')
    op.drop_table('Genre')
    op.drop_index(op.f('ix_Category_id'), table_name='Category')
    op.drop_table('Category')
    # ### end Alembic commands ###