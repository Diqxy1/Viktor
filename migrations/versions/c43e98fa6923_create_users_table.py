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
        sa.Column('uuid', sa.String(36), nullable=False, unique=True, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('document', sa.String(22), nullable=False, unique=True),
        sa.Column('password', sa.String(255), nullable=False),

        sa.Column('email', sa.String(100), nullable=True, unique=True),
        sa.Column('verified_email', sa.Boolean, default=True),

        sa.Column('phone', sa.String(20), nullable=True, unique=True),
        sa.Column('verified_phone', sa.Boolean, default=False),

        sa.Column('is_active', sa.Boolean, default=False),
        sa.Column('code_reference', sa.String(20), nullable=False, unique=True),

        # cli step
        sa.Column('is_staff', sa.Boolean, default=False),

        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('users')
