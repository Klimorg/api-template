from typing import List

from fastapi import APIRouter, status

from app.models.inference import InferenceIn, InferenceOut
from app.factories.models import FakeModel

router = APIRouter()

model = FakeModel()


@router.post(
    "/",
    tags=["tags"],
    response_model=List[InferenceOut],
    status_code=status.HTTP_201_CREATED,
    summary="resume",
)
async def create_inference(datas: List[InferenceIn]):

    datas_dict = [data.dict() for data in datas]
    predictions = model.predict(datas_dict)
    result = [InferenceOut(**prediction) for prediction in predictions]
    return result


# @router.get(
#     "/",
#     tags=["tags"],
#     response_model=List[BaseRead],
#     status_code=status.HTTP_200_OK,
#     summary="resume",
# )
# async def get_inference():
#     return [
#         BaseRead(
#             **{
#                 "inference_date": "2022-09-05",
#                 "inference_time": "15:07:18",
#                 "num": 0,
#                 "id": "0b272c24-327c-4850-add6-1b628e58c64f",
#             },
#         ),
#     ]
