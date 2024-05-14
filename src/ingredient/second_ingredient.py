import collections


import argparse
import json
import os


def second_most_used_ingredient(recipes):
    """
    This function takes a dictionary of recipes as input, where each recipe
    is represented as a list of ingredients. It returns the second most
    commonly used ingredient in the recipes.

    Parameters:
    recipes (dict): A dictionary where the keys are the names of the recipes
                    and the values are lists of ingredients.

    Returns:
    str: The second most commonly used ingredient in the recipes.
    """
    # if the input is not a dictionary raise an error
    if not isinstance(recipes, dict):
        raise TypeError("Input must be a dictionary")
    
    # if the input is an empty dictionary return none
    if not recipes:
        return None
    
    # Create a Counter object to count the number of occurrences of each
    # ingredient in the recipes.
    ingredient_counts = collections.Counter()

    # Iterate over each recipe in the recipes dictionary.
    for recipe in recipes.values():
        # Update the ingredient counts by incrementing the count of each
        # ingredient in the recipe.
        ingredient_counts.update(recipe)
    print(ingredient_counts)    
    # Get the second most commonly used ingredient from the ingredient counts.
    # The most_common() method returns a list of tuples, where each tuple
    # contains an ingredient and its count. We access the second tuple in the
    # list (index 1) to get the second most used ingredient.
    # second_most_used = ingredient_counts.most_common()[1][0]

    # assign the count of the first ingredient in the list to cnt
    cnt = ingredient_counts.most_common()[0][1]

    # iterate over ingredient counts and return the first ingredient for which the count is different from cnt
    for ingredient, count in ingredient_counts.most_common():
        if count != cnt:
            second_most_used = ingredient
            break
        

    # Return the second most used ingredient.
    return second_most_used


def main():
    parser = argparse.ArgumentParser(description="Find the second most "
                                                 "used ingredient in a list "
                                                 "of recipes.")
    parser.add_argument("recipes_file", help="Path to a JSON file containing "
                                             "a dictionary of recipes.")
    args = parser.parse_args()

    # Read the input recipes from the JSON file.
    with open(args.recipes_file, "r") as f:
        recipes = json.load(f)

    # Find the second most used ingredient in the recipes.
    second_most_used = second_most_used_ingredient(recipes)

    # Print the second most used ingredient to the console.
    print(second_most_used)


# Only run the main function if this script is executed directly.
if __name__ == "__main__":
    main()

