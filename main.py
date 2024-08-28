"""Docstring"""
import json
def load_recipe(recipe):
    recipe_dictionary = json.loads(recipe)
    return recipe_dictionary

def adjust_recipe(recipe,number_of_people):
    if recipe['servings'] == number_of_people:
        return recipe
    else:
        multiplicator = number_of_people / recipe['servings']
        recipe_new = recipe
        recipe_new["ingredients"]["Spaghetti"] = recipe_new["ingredients"]["Spaghetti"] * multiplicator
        recipe_new["ingredients"]["Tomato Sauce"] = recipe_new["ingredients"]["Tomato Sauce"] * multiplicator
        recipe_new["ingredients"]["Minced Meat"] = recipe_new["ingredients"]["Minced Meat"] * multiplicator
        recipe_new["servings"] = number_of_people

    return recipe_new


if __name__ == '__main__':
        recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
        new_recipe = (load_recipe(recipe_json))
        print(new_recipe["ingredients"]["Spaghetti"])
        adjust_recipe(new_recipe,1)