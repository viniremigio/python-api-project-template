from typing import Dict

from app.model import Recipe, User


def load_user_database() -> Dict[str, User]:
    return {
        "1": User(
            id=1,
            recipes=[
                Recipe(
                    title="Egg Sandwitch",
                    ingredients=[{"eggs": 2, "bread": 2}],
                    category="breakfast",
                ),
                Recipe(
                    title="Coffee with Sugar",
                    ingredients=[{"Coffee": 1, "Sugar": 1}],
                    category="breakfast",
                ),
            ],
        ),
        "2": User(
            id=2,
            recipes=[
                Recipe(
                    title="Pesto Pasta",
                    ingredients=[{"Pasta": 1, "Pesto": 1, "Butter": 1}],
                    category="lunch",
                )
            ],
        ),
    }
