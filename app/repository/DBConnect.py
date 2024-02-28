from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnect:
    # Create a sessionmaker bound to the database engine
    engine = create_engine('sqlite:///stocks.db')  # Replace with your actual database connection string
    Session = sessionmaker(bind=engine)
