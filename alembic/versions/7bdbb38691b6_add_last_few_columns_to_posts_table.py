"""add last few columns to posts table

Revision ID: 7bdbb38691b6
Revises: a6cf6c9f9ef7
Create Date: 2022-06-07 21:00:46.950122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bdbb38691b6'
down_revision = 'a6cf6c9f9ef7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = 'True'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False,
    server_default = sa.text('NOW()')),)


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
