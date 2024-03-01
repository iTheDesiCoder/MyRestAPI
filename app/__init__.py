# Desc: Main entry point for the application
from fastapi import FastAPI
from debug_toolbar.middleware import DebugToolbarMiddleware
from app.globalexceptionhandler import GlobalExceptionHandler
from app.contoller import stock_router

app = FastAPI(debug=True)
app.add_middleware(DebugToolbarMiddleware)
app.exception_handler(Exception)(GlobalExceptionHandler.exception_handler)
app.include_router(stock_router)
