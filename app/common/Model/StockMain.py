from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()


# Define the Stock model
class StockMain(Base):
    __tablename__ = 'StockMain'

    id = Column(Integer, primary_key=True)
    nasdaq_traded = Column(String)
    security_name = Column(String)
    listing_exchange = Column(String)
    market_category = Column(String)
    etf = Column(String)
    round_lot_size = Column(Integer)
    test_issue = Column(String)
    financial_status = Column(String)
    cqs_symbol = Column(String)
    nasdaq_symbol = Column(String)
    next_shares = Column(String)



