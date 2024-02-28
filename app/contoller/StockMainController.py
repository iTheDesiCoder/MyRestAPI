from flask import Blueprint, jsonify, request
from flasgger import swag_from

stock_blueprint = Blueprint('stocks', __name__)


class StockMainController:
    @stock_blueprint.route('/stocks', methods=['GET'])
    @swag_from('docs/StockMain/get_stocks.yml')
    def get_stocks():
        # Your code to fetch and return stocks goes here
        pass

    @stock_blueprint.route('/stocks', methods=['POST'])
    @swag_from('docs/StockMain/add_stock.yml')
    def add_stock():
        # Your code to add a new stock goes here
        pass