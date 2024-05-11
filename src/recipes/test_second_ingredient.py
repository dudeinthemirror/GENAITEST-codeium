import json
import pytest

from second_ingredient import second_most_used_ingredient

@pytest.fixture
def recipes():
    with open("./src/recipes/recipes.json") as f:
        return json.load(f)

def test_single_ingredient(recipes):
    assert second_most_used_ingredient(recipes) == "flour"

def test_two_ingredients_different_counts(recipes):
    recipes["recipe2"] = ["ingredient1", "ingredient3"]
    assert second_most_used_ingredient(recipes) == "flour"

def test_multiple_ingredients(recipes):
    recipes["recipe3"] = ["ingredient1", "ingredient2", "ingredient5"]
    assert second_most_used_ingredient(recipes) == "flour"

def test_empty_dict(recipes):
    empty_dict = {}
    assert second_most_used_ingredient(empty_dict) is None

def test_input_not_dict():
    with pytest.raises(TypeError):
        second_most_used_ingredient([])

