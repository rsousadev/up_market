from fastapi import APIRouter

from ..apis.api_product import router as api_product_router

router = APIRouter()
router.include_router(api_product_router)
