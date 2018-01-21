"""empty message

Revision ID: 6393be6e7b25
Revises:
Create Date: 2018-01-20 18:32:49.426413

"""
from alembic import op
import sqlalchemy as sa


***REMOVED*** revision identifiers, used by Alembic.
revision = '6393be6e7b25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ***REMOVED*** ***REMOVED******REMOVED******REMOVED*** commands auto generated by Alembic - please adjust! ***REMOVED******REMOVED******REMOVED***
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('icon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shortname', sa.String(length=20), nullable=True),
    sa.Column('mimetype', sa.String(length=20), nullable=True),
    sa.Column('image_filename', sa.String(length=500), nullable=True),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('repo_type', sa.String(length=20), nullable=True),
    sa.Column('url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('repo_type'),
    sa.UniqueConstraint('url')
    )
    ***REMOVED*** ***REMOVED******REMOVED******REMOVED*** end Alembic commands ***REMOVED******REMOVED******REMOVED***


def downgrade():
    ***REMOVED*** ***REMOVED******REMOVED******REMOVED*** commands auto generated by Alembic - please adjust! ***REMOVED******REMOVED******REMOVED***
    op.drop_table('source')
    op.drop_table('icon')
    op.drop_table('category')
    ***REMOVED*** ***REMOVED******REMOVED******REMOVED*** end Alembic commands ***REMOVED******REMOVED******REMOVED***
