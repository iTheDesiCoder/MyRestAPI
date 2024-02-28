# Desc: Main entry point for the application
from flask import Flask
from .contoller.StockMainController import stock_blueprint
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(stock_blueprint)
swagger = Swagger(app)