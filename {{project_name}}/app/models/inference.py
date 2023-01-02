import uuid
from datetime import date, time

import arrow
from pydantic import UUID4, BaseModel, Field


class InferenceBase(BaseModel):
    pass


class InferenceIn(InferenceBase):
    data: int = Field(nullable=True)


class InferenceOut(InferenceBase):
    inference_date: date = Field(default=arrow.now().format("YYYY-MM-DD"))
    inference_time: time = Field(default=arrow.now().format("HH:mm:ss"))
    id: UUID4 = Field(default_factory=uuid.uuid4)
    num: int = Field(nullable=True)


# class BaseRead(Base):
#     id: UUID4 = Field(default_factory=uuid.uuid4)
