from typing import List

from fastapi import APIRouter, status

from app.pydantic_models import BaseCreateInput, BaseCreateOutput, BaseRead

router = APIRouter()


@router.post(
    "/",
    tags=["tags"],
    response_model=BaseCreateOutput,
    status_code=status.HTTP_201_CREATED,
    summary="resume",
)
async def create_inference(placeholder: BaseCreateInput):
    return BaseCreateOutput(**placeholder.dict())


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
                "id": "0b272c24-327c-4850-add6-1b628e58c64f",
            },
        ),
    ]
