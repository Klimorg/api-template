from datetime import date, datetime, time
import uuid
import arrow
from pydantic import BaseModel, Field, UUID4


class Base(BaseModel):
    inference_date: date = Field(default=arrow.now().format("YYYY-MM-DD"))
    inference_time: time = Field(default=arrow.now().format("HH:mm:ss"))
    num: int = Field(nullable=True)


class BaseCreateInput(Base):
    pass


class BaseCreateOutput(Base):
    id: UUID4 = Field(default_factory=uuid.uuid4)


class BaseRead(Base):
    id: UUID4 = Field(default_factory=uuid.uuid4)


class DeploymentInfo(BaseModel):
    deployment_commit: str
    deployment_date: datetime
    api_version: str
