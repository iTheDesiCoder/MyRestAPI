from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app.manager import StockMainManager

stock_blueprint = Blueprint('stocks', __name__)


class StockMainController:
    @stock_blueprint.route('/stocks/get_stocks', methods=['GET'])
    @swag_from('docs/get_stocks.yml')
    def get_stocks():
        stock_manager = StockMainManager()
        stock_main_dtos = stock_manager.get_stocks()
        return jsonify(stock_main_dtos)
