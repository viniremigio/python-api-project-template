from typing import List

import pytest

from app.model import Recipe
from app.service import RecipeService


@pytest.fixture
def expected_output():
    return Recipe(
        title="Egg Sandwitch",
        ingredients=[{"eggs": 2, "bread": 2}],
        category="breakfast",
    )


def test_get_recipe():
    service: RecipeService = RecipeService()
    recipes: List[Recipe] = service.list_recipes_by_user_id(user_id=1)
    assert recipes[0] == expected_output
