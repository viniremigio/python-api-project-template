from typing import Dict, List, Optional

from pydantic import BaseModel


class Recipe(BaseModel):
    title: str
    ingredients: List[Dict[str, int]]
    category: str


class User(BaseModel):
    id: int
    recipes: Optional[List[Recipe]]
