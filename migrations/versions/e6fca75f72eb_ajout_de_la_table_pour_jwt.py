"""Ajout de la table pour jwt

Revision ID: e6fca75f72eb
Revises: d1c7e2101921
Create Date: 2020-07-02 13:34:47.770080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6fca75f72eb'
down_revision = 'd1c7e2101921'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('slug', sa.String(length=15), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'slug')
    # ### end Alembic commands ###