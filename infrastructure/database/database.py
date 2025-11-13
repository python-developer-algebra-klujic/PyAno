from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DATABASE_PATH


engine = create_engine(DATABASE_PATH)
Base = declarative_base()

Session = sessionmaker(bind=engine)
