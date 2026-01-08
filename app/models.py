from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.database import Base
import sqlalchemy

# app/models.py
from app.database import Base
from sqlalchemy import Column, Integer, String, Text

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(Text)

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/article_db"

engine = create_async_engine(DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()
