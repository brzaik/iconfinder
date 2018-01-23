"""empty message

Revision ID: 440cf49df8ee
Revises: 688786b5bd0d
Create Date: 2018-01-21 15:44:49.432639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '440cf49df8ee'
down_revision = '688786b5bd0d'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('icon', 'shortname', existing_type=sa.String(20), type_=sa.String(500))


def downgrade():
    op.alter_column('icon', 'shortname', existing_type=sa.String(500), type_=sa.String(20))
