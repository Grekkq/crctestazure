import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

if os.getenv("CONNECTION_STRING"):
    SQLALCHEMY_DATABASE_URL = os.getenv("CONNECTION_STRING")
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234@host.docker.internal:5432/fastapidb"

print(f"connection string: ${SQLALCHEMY_DATABASE_URL}")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()