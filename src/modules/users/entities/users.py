import sqlalchemy as sa

from src.config.database import Base

class User(Base):

    __tablename__ = 'users'

    uuid = sa.Column(sa.String, primary_key=True, unique=True, index=True)
    name = sa.Column(sa.String)
    document = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)

    email = sa.Column(sa.String, nullable=True, unique=True)
    verified_email = sa.Column(sa.Boolean, default=False)

    phone = sa.Column(sa.String, nullable=True, unique=True)
    verified_phone = sa.Column(sa.Boolean, default=False)

    is_active = sa.Column(sa.Boolean, default=False)
    code_reference = sa.Column(sa.String, nullable=False, unique=True)

    is_staff = sa.Column(sa.Boolean, default=True)

    created_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, nullable=False, server_default=sa.func.now(), server_onupdate=sa.func.now())
