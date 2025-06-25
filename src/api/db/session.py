import sqlmodel
from sqlmodel import SQLModel, Session
import timescaledb

from .config import DATABASE_URL, DB_TIMEZONE

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL needs to be set")

engine = timescaledb.create_engine(DATABASE_URL, timezone=DB_TIMEZONE)

import time

def wait_for_db(max_retries=10, delay=2):
    for attempt in range(max_retries):
        try:
            with engine.connect():
                print("✅ Database is available.")
                return True
        except Exception:
            print(f"⏳ Waiting for DB... attempt {attempt + 1}/{max_retries}")
            time.sleep(delay)
    print("❌ Could not connect to the database.")
    return False

def init_db():
    if not wait_for_db():
        return
    print("creating database")
    SQLModel.metadata.create_all(engine)
    print("creating hypertables")
    timescaledb.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session