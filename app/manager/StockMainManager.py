class StockMainManager:
    def get_stocks():
        # Use the StockRepository to fetch stocks
        stock_repository = StockRepository()
        stocks = stock_repository.get_stocks()

