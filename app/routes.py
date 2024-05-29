from typing import List, Optional

from fastapi import APIRouter, HTTPException

from app.model import Recipe
from app.service import RecipeService
from app.logger import Logger

service = RecipeService()
router = APIRouter()
logger = Logger()


@router.get("/")
def hello():
    return "Hello World!"


@router.get("/user/{user_id}/recipes")
async def get_recipes_by_user(user_id: str) -> Optional[List[Recipe]]:
    recipes = service.list_recipes_by_user_id(user_id=user_id)
    if not recipes:
        logger.warning(f"recipes=not_found")
        raise HTTPException(status_code=404, detail="Recipes not found")
    logger.info(f"recipes={recipes}")
    return recipes
