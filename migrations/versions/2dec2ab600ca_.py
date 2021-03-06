"""empty message

Revision ID: 2dec2ab600ca
Revises: 
Create Date: 2018-07-14 22:08:33.099851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dec2ab600ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loan_providers',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('amountCapable', sa.String(length=50), nullable=True),
    sa.Column('loanType', sa.String(length=50), nullable=True),
    sa.Column('collateralType', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('user',
    sa.Column('firstName', sa.String(length=50), nullable=False),
    sa.Column('lastName', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('occupation', sa.String(length=50), nullable=True),
    sa.Column('dateJoined', sa.String(length=10), nullable=True),
    sa.Column('netSalary', sa.Integer(), nullable=True),
    sa.Column('loanType', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('IDnumber', sa.String(length=50), nullable=True),
    sa.Column('phoneNumber', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('firstName')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('loan_providers')
    # ### end Alembic commands ###
