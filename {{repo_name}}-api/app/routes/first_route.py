from typing import List

from app.pydantic_models import BaseCreate, BaseRead
from fastapi import APIRouter, status

router = APIRouter()


@router.post(
    "/",
    tags=["tags"],
    response_model=BaseRead,
    status_code=status.HTTP_201_CREATED,
    summary="resume",
)
async def create_inference(placeholder: BaseCreate):
    return BaseRead(**placeholder.dict())


@router.get(
    "/",
    tags=["tags"],
    response_model=List[BaseRead],
    status_code=status.HTTP_200_OK,
    summary="resume",
)
async def get_inference():
    return [
        BaseRead(
            **{
                "inference_date": "2022-09-05",
                "inference_time": "15:07:18",
                "num": 0,
            }
        )
    ]
