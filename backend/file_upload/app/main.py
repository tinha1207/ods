from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.api_v1.endpoints import file_upload

app = FastAPI()

app.include_router(file_upload.router)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
