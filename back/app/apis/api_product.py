from typing import List

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=200)
async def create_product() -> dict:
    return {"Hello": "World"}
