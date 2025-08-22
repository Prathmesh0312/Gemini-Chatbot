from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#Base class must be defined
class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///./agent.db", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
