from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Change credentials as per your PostgreSQL setup
DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/Training"

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
