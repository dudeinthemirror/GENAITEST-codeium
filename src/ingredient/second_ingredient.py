import json
import sys

def second_most_used_ingredient(recipes):
    """
    Given a dictionary of recipes, where each recipe is a list of ingredients, 
    this function returns the second most commonly used ingredient across all recipes.
    
    Parameters:
    - recipes (dict): A dictionary where the keys are recipe names and the values are lists of ingredients.
    
    Returns:
    - str: The second most commonly used ingredient across all recipes.
    
    Example:
    recipes = {
        "pie": ["flour", "pepperoni", "tomato", "cheese", "salt", "pepper"],
        "cake": ["flour", "milk", "sugar", "cheese"],
        "icecream": ["milk", "sugar", "nuts"],
        "soup": ["water", "meat", "salt", "pepper", "potatoes"],
        "fries": ["potatoes", "salt"],
        "salad": ["lettuce", "tomato", "cucumber", "onion", "oil", "salt", "pepper"],
        "pasta": ["flour", "water", "sauce", "pepper", "salt"]
    }
    second_most_used_ingredient(recipes) -> "salt"
    """
    # if the input is not a dictionary, raise an error
    if not isinstance(recipes, dict):
        raise TypeError("Input must be a dictionary")
    
    # if the input is an empty dictionary, return none
    if not recipes:
        return None
    
    # Create an empty dictionary to store the counts of each ingredient
    ingredient_counts = {}

    # Iterate over each recipe in the recipes dictionary
    for recipe in recipes.values():
        # Iterate over each ingredient in the current recipe
        for ingredient in recipe:
            # Increment the count of the current ingredient
            ingredient_counts[ingredient] = ingredient_counts.get(ingredient, 0) + 1

    # Sort the ingredient counts in descending order
    # The key function passed to sorted() sorts the counts in descending order
    sorted_counts = sorted(ingredient_counts.items(), key=lambda x: x[1], reverse=True)
    print(sorted_counts)

    # (luc) This section had to be refactored by hand. The original code did not 
    # handle the case where there are multiple most used ingredients with the same count.

    # assign the count of the first ingredient in the sorted list to cnt
    cnt = sorted_counts[0][1]

    # iterate through sorted_ingredients and return the first ingredient for which the count is different from cnt
    for ingredient, count in sorted_counts:
        if count != cnt:
            return ingredient
        
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python second_ingredient.py <recipes.json>")
        sys.exit(1)

    # Get the path to the recipes JSON file from the command-line argument
    recipes_file = sys.argv[1]

    try:
        # Open the recipes JSON file and load the contents into a dictionary
        with open(recipes_file) as f:
            recipes = json.load(f)

        # Call the second_most_used_ingredient function and print the result
        result = second_most_used_ingredient(recipes)
        print(f"The second most used ingredient is: {result}")

    except FileNotFoundError:
        print(f"Error: The file '{recipes_file}' was not found.")
        sys.exit(1)

    except json.JSONDecodeError:
        print(f"Error: The file '{recipes_file}' is not a valid JSON file.")
        sys.exit(1)

