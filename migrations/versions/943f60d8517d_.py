"""empty message

Revision ID: 943f60d8517d
Revises: 292a3c2c3e9c
Create Date: 2018-06-08 03:19:42.344311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '943f60d8517d'
down_revision = '292a3c2c3e9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('Cid', sa.Integer(), nullable=False),
    sa.Column('kota', sa.String(length=60), nullable=True),
    sa.Column('provinsi', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('Cid')
    )
    op.create_index(op.f('ix_cities_kota'), 'cities', ['kota'], unique=False)
    op.create_index(op.f('ix_cities_provinsi'), 'cities', ['provinsi'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('nama_depan', sa.String(length=60), nullable=True),
    sa.Column('nama_belakang', sa.String(length=60), nullable=True),
    sa.Column('kota_Cid', sa.Integer(), nullable=True),
    sa.Column('tanggal_lahir', sa.Date(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_kost_owner', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['kota_Cid'], ['cities.Cid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_nama_belakang'), 'users', ['nama_belakang'], unique=False)
    op.create_index(op.f('ix_users_nama_depan'), 'users', ['nama_depan'], unique=False)
    op.create_index(op.f('ix_users_tanggal_lahir'), 'users', ['tanggal_lahir'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('kosts',
    sa.Column('Kid', sa.Integer(), nullable=False),
    sa.Column('Kname', sa.String(length=60), nullable=True),
    sa.Column('Kaddress', sa.String(length=100), nullable=True),
    sa.Column('city_Cid', sa.Integer(), nullable=True),
    sa.Column('Kphone', sa.String(length=20), nullable=True),
    sa.Column('Kprice', sa.Integer(), nullable=True),
    sa.Column('Kprice_range', sa.Integer(), nullable=True),
    sa.Column('Ktype', sa.String(length=20), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Kverified', sa.Boolean(), nullable=True),
    sa.Column('Klat', sa.DECIMAL(precision=10, scale=8), nullable=True),
    sa.Column('Klng', sa.DECIMAL(precision=11, scale=8), nullable=True),
    sa.ForeignKeyConstraint(['city_Cid'], ['cities.Cid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('Kid')
    )
    op.create_index(op.f('ix_kosts_Kaddress'), 'kosts', ['Kaddress'], unique=False)
    op.create_index(op.f('ix_kosts_Kname'), 'kosts', ['Kname'], unique=False)
    op.create_index(op.f('ix_kosts_Kprice_range'), 'kosts', ['Kprice_range'], unique=False)
    op.create_index(op.f('ix_kosts_Kprice'), 'kosts', ['Kprice'], unique=False)
    op.create_index(op.f('ix_kosts_Ktype'), 'kosts', ['Ktype'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_kosts_Ktype'), table_name='kosts')
    op.drop_index(op.f('ix_kosts_Kprice'), table_name='kosts')
    op.drop_index(op.f('ix_kosts_Kprice_range'), table_name='kosts')
    op.drop_index(op.f('ix_kosts_Kname'), table_name='kosts')
    op.drop_index(op.f('ix_kosts_Kaddress'), table_name='kosts')
    op.drop_table('kosts')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_tanggal_lahir'), table_name='users')
    op.drop_index(op.f('ix_users_nama_depan'), table_name='users')
    op.drop_index(op.f('ix_users_nama_belakang'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_cities_provinsi'), table_name='cities')
    op.drop_index(op.f('ix_cities_kota'), table_name='cities')
    op.drop_table('cities')
    # ### end Alembic commands ###
