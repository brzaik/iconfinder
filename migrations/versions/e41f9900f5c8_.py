"""empty message

Revision ID: e41f9900f5c8
Revises: 440cf49df8ee
Create Date: 2018-01-21 15:59:52.541522

"""
from alembic import op
import sqlalchemy as sa


***REMOVED*** revision identifiers, used by Alembic.
revision = 'e41f9900f5c8'
down_revision = '440cf49df8ee'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint("repo_type", "source", "unique")


def downgrade():
    op.create_unique_constraint("repo_type", "source", ["repo_type"])
