from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydb.db", echo=True)
sync_session = sessionmaker(engine, expire_on_commit=False)


def get_session():
    with sync_session() as session:
        yield session
