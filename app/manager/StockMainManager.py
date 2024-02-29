from app.repository import StockMainRepository
from app.common.DTO import StockMainDto

class StockMainManager:
    def get_stocks(self):
        # Use the StockRepository to fetch stocks
        stock_repository = StockMainRepository()
        stock_main_dtos = stock_repository.get_stocks()
        return stock_main_dtos
