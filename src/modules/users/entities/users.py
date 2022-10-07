import sqlalchemy as sa

from src.config.database import Base

class User(Base):

    __tablename__ = 'users'

    uuid = sa.Column(sa.String, primary_key=True, index=True)
    email = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
    name = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
