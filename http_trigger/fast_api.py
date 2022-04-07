from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.presentation.controller import example_controller as examples

fast_app = FastAPI()
fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
fast_app.include_router(examples.router)
