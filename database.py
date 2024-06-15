import os
import sys

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
# sys.path.append(BASE_DIR)


class Database:
    def __init__(self):
        print("initialize db instance")
        load_dotenv()
        # SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
        SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
        engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        self.Base = declarative_base(engine)

    def getBase(self):
        return self.Base

    def getSession(self):
        return self.SessionLocal()
