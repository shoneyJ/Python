from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os, sys
from dotenv import load_dotenv

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
# sys.path.append(BASE_DIR)
load_dotenv()

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()