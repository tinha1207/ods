from fastapi import FastAPI

from app.api.api_v1 import address, record

app = FastAPI()

app.include_router(address.router)
app.include_router(record.router)
