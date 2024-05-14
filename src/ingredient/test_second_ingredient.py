import json
import pytest
from src.ingredient.second_ingredient import second_most_used_ingredient
@pytest.fixture
def recipes():
    with open("./src/ingredient/recipes.json", "r") as f:
        return json.load(f)

def test_second_most_used_ingredient(recipes):
    assert second_most_used_ingredient(recipes) == "flour"

    # Test case where the input is not a dictionary
    with pytest.raises(TypeError):
        second_most_used_ingredient([])

    # Test case where the input is an empty dictionary
    assert second_most_used_ingredient({}) is None
