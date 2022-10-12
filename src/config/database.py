import logging

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.config.database_url import DatabaseUrl

logger = logging.getLogger(__name__)

db = DatabaseUrl().get_database_url()
db_engine = create_async_engine(db)
db_session = sessionmaker(autocommit=False, bind=db_engine, class_=AsyncSession)

Base = declarative_base(bind=db_engine)

async def get_database():
    db = db_session()
    try:
        yield db
    finally:
        await db.close()
