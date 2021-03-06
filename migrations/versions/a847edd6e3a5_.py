"""empty message

Revision ID: a847edd6e3a5
Revises: 90e6c7d95489
Create Date: 2017-12-31 23:00:45.746898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a847edd6e3a5'
down_revision = '90e6c7d95489'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kosts', sa.Column('Kverified', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_kosts_Kaddress'), 'kosts', ['Kaddress'], unique=False)
    op.create_index(op.f('ix_kosts_Kname'), 'kosts', ['Kname'], unique=False)
    op.drop_index('ix_kosts_Kaddress', table_name='kosts')
    op.drop_index('ix_kosts_Kname', table_name='kosts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_kosts_Kname', 'kosts', ['Kname'], unique=False)
    op.create_index('ix_kosts_Kaddress', 'kosts', ['Kaddress'], unique=False)
    op.drop_index(op.f('ix_kosts_Kname'), table_name='kosts')
    op.drop_index(op.f('ix_kosts_Kaddress'), table_name='kosts')
    op.drop_column('kosts', 'Kverified')
    # ### end Alembic commands ###
