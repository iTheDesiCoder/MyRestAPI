from app.common.DTO import StockMainDto
from app.common.Model import StockMain
from app.repository import DBConnect


class StockMainRepository:
    def get_stocks(self):
        session = DBConnect.Session()
        stock_mains = session.query(StockMain).all()
        session.close()
        stock_main_dtos = [StockMainDto.from_model(stock_main) for stock_main in stock_mains]
        return stock_main_dtos
