from app.repository import DBConnect


class StockMainRepository:
    def get_stocks(self):
        session = DBConnect.Session()
        stocks = session.query(StockMain).all()
        session.close()
        return stocks