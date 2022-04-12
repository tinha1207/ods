from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1 import address, record, transaction

app = FastAPI()

origins = ["http://localhost:8001/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(address.router)
app.include_router(record.router)
app.include_router(transaction.router)
