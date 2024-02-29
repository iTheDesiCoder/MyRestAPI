from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import CONNECTION_STRING


class DBConnect:
    # Create a sessionmaker bound to the database engine
    engine = create_engine(CONNECTION_STRING)
    Session = sessionmaker(bind=engine)
