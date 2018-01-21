"""empty message

Revision ID: c95bd3747a97
Revises: 6393be6e7b25
Create Date: 2018-01-20 19:41:53.559578

"""
from alembic import op
import sqlalchemy as sa


***REMOVED*** revision identifiers, used by Alembic.
revision = 'c95bd3747a97'
down_revision = '6393be6e7b25'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('icon', sa.Column('localpath', sa.String(500)))
    op.add_column('icon', sa.Column('source_id', sa.Integer, sa.ForeignKey('source.id')))


def downgrade():
    op.drop_constraint('icon_ibfk_1', 'icon', type_='foreignkey')
    op.drop_column('icon', 'source_id')
    op.drop_column('icon', 'localpath')
