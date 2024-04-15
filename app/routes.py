from typing import List, Optional

from fastapi import APIRouter, HTTPException

from app.model import Recipe
from app.service import RecipeService

service = RecipeService()
router = APIRouter()


@router.get("/")
def hello():
    return "Hello World!"


@router.get("/user/{user_id}/recipes")
async def get_recipes_by_user(user_id: str) -> Optional[List[Recipe]]:
    recipes = service.list_recipes_by_user_id(user_id=user_id)
    if not recipes:
        raise HTTPException(status_code=404, detail="Recipes not found")
    return recipes
