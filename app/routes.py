from typing import List, Optional

from fastapi import APIRouter

from app.model import Recipe
from app.service import RecipeService

router = APIRouter()


class RecipeController:
    def __init__(self) -> None:
        self.service = RecipeService()

    @router.get("/")
    def hello(self):
        return "Hello World!"

    @router.get("/user/{user_id}/recipes")
    async def get_recipes_by_user(self, user_id: int) -> Optional[List[Recipe]]:
        return self.service.list_recipes_by_user_id(user_id=user_id)
