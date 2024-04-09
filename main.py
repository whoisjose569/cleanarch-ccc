from fastapi import FastAPI
from src.main.routes.routes import router

app = FastAPI()

app.include_router(router)