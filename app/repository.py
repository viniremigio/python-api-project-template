from typing import List, Optional

from app.model import Recipe, User
from app.utils import load_user_database


class RecipeRepository:
    def __init__(self) -> None:
        self.repo = load_user_database()

    def get_user_recipes(self, user_id: str) -> Optional[List[Recipe]]:
        user: Optional[User] = self.repo.get(user_id)
        recipes = (
            user.recipes if user is not None and hasattr(user, "recipes") else None
        )
        return recipes
