"""create posts table

Revision ID: e7058aa3e1f7
Revises: 
Create Date: 2022-06-07 18:46:38.212882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7058aa3e1f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),nullable = False, primary_key = True),
    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
