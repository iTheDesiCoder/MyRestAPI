# Desc: Main entry point for the application
from flask import Flask
from flasgger import Swagger
from app.contoller import stock_blueprint

app = Flask(__name__)
app.register_blueprint(stock_blueprint)
swagger = Swagger(app)
