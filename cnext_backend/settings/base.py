from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import config

DB_NAME = config.getEnv("MASTER_DB_NAME")
DB_USER = config.getEnv("MASTER_DB_USER")
DB_PASSWORD = config.getEnv("MASTER_DB_PASSWORD")
DB_HOST = config.getEnv("MASTER_DB_HOST")
DB_PORT = config.getEnv("MASTER_DB_PORT")

# SQLALCHEMY_DATABASE_URL = f'mysql://staging:cklp0874*&$(#%3rxv?@stagingdb2.mycareers360.com:3306/django360'

SQLALCHEMY_DATABASE_URL = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
