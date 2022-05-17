from sqlmodel import SQLModel
# import  models
from database import engine


def create_db_table():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_table()
