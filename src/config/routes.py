from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.modules.users import routes as user_router

def init_app(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user_router.router)
