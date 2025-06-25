from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI

from api.events.routing import router as event_router
from api.db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup up
    init_db()
    yield
    # clean up

app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix='/api/events')
# /api/events


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/healthy")
def health_check():
    return {"health status": "Ok"}