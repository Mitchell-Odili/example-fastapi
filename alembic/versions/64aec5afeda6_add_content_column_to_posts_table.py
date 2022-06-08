"""add content column to posts table

Revision ID: 64aec5afeda6
Revises: e7058aa3e1f7
Create Date: 2022-06-07 19:02:23.812218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64aec5afeda6'
down_revision = 'e7058aa3e1f7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))


def downgrade():
    op.drop_column('posts', 'content')
