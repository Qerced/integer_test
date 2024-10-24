from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base

engine = create_engine(
    'mssql+pymssql://sa:password123@localhost/?charset=utf8'
)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
