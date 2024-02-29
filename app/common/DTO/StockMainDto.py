from dataclasses import dataclass


@dataclass
class StockMainDto:
    symbol: str
    nasdaq_traded: str
    security_name: str
    listing_exchange: str
    market_category: str
    etf: str
    round_lot_size: int
    test_issue: str
    financial_status: str
    cqs_symbol: str
    nasdaq_symbol: str
    nextshares: str

    @classmethod
    def from_model(cls, model):
        return cls(
            symbol=model.symbol,
            nasdaq_traded=model.nasdaq_traded,
            security_name=model.security_name,
            listing_exchange=model.listing_exchange,
            market_category=model.market_category,
            etf=model.etf,
            round_lot_size=model.round_lot_size,
            test_issue=model.test_issue,
            financial_status=model.financial_status,
            cqs_symbol=model.cqs_symbol,
            nasdaq_symbol=model.nasdaq_symbol,
            nextshares=model.nextshares,
        )
