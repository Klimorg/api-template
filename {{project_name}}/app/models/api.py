from datetime import datetime
from pydantic import BaseModel


class DeploymentInfo(BaseModel):
    deployment_commit: str
    deployment_date: datetime
    api_version: str
