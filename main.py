from fastapi import FastAPI
from cnext_backend.apps.abroad_listing import controllers

app = FastAPI()

app.include_router(controllers.router)


