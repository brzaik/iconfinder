"""empty message

Revision ID: 688786b5bd0d
Revises: c95bd3747a97
Create Date: 2018-01-21 15:17:32.402797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '688786b5bd0d'
down_revision = 'c95bd3747a97'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('icon', sa.Column('category_id', sa.Integer, sa.ForeignKey('category.id')))


def downgrade():
    op.drop_constraint('icon_ibfk_2', 'icon', type_='foreignkey')
    op.drop_column('icon', 'category_id')
