from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()

@router.get("/")
def read_events():
    return {"results": [{'id': 1}, {'id': 2}]}


@router.post("/")
def create_events(payload: EventCreateSchema):
    data = payload.model_dump()
    return {'id': 1, **data}


@router.put("/{event_id}")
def update_events(event_id: int, payload: EventUpdateSchema):
    data = payload.model_dump()
    return {'id': event_id, **data}

@router.get("/{event_id}")
def get_event(event_id: int):
    """

    :type event_id: int
    """
    return {'id': event_id}