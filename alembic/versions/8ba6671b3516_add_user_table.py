"""add user table

Revision ID: 8ba6671b3516
Revises: 64aec5afeda6
Create Date: 2022-06-07 19:11:57.300024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ba6671b3516'
down_revision = '64aec5afeda6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable = False),
                    sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default = sa.text('now()'),
                                 nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
