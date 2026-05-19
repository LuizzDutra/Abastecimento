from pydantic import BaseModel


class StatusSchema(BaseModel):
    version: str
    status: int
    database: int
