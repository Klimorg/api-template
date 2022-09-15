from datetime import date, datetime, time

import arrow
from pydantic import BaseModel, Field


class Base(BaseModel):
    inference_date: date = Field(default=arrow.now().format("YYYY-MM-DD"))
    inference_time: time = Field(default=arrow.now().format("HH:mm:ss"))
    num: int = Field(nullable=True)


class BaseCreate(Base):
    pass


class BaseRead(Base):
    pass


class DeploymentInfo(BaseModel):
    deployment_commit: str
    deployment_date: datetime
