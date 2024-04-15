from typing import List, Optional

from app.model import Recipe
from app.repository import RecipeRepository


class RecipeService:
    def __init__(self) -> None:
        self.repo = RecipeRepository()

    def list_recipes_by_user_id(self, user_id: str) -> Optional[List[Recipe]]:
        results: Optional[List[Recipe]] = self.repo.get_user_recipes(user_id=user_id)
        return results
