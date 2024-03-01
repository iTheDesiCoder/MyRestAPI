from fastapi import APIRouter
from app.manager import StockMainManager
from app.common.DTO import StockMainDto
from typing import List

stock_router = APIRouter()


class StockMainController:
    @stock_router.get("/get_stocks", status_code=200, response_model=List[StockMainDto])
    async def get_stocks():
        stock_manager = StockMainManager()
        stock_main_dtos = stock_manager.get_stocks()
        return stock_main_dtos
