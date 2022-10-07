"""create users table

Revision ID: c43e98fa6923
Revises:
Create Date: 2022-10-07 10:09:15.521562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c43e98fa6923'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('uuid', sa.String(36), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(60), nullable=False),
        sa.Column('password', sa.String(30), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade() -> None:
    op.drop_table('users')
