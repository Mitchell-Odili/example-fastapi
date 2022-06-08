"""add foreign-key to post table

Revision ID: a6cf6c9f9ef7
Revises: 8ba6671b3516
Create Date: 2022-06-07 20:01:58.038216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6cf6c9f9ef7'
down_revision = '8ba6671b3516'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table='users', 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
