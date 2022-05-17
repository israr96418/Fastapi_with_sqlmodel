from sqlmodel import create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


engine = create_engine(sqlite_url, echo=True)

SessionLocal = Session(bind=engine)


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
