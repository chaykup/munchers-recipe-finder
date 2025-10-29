from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import sys

load_dotenv()
API_KEY=os.getenv("API_KEY")
base_url = 'https://www.themealdb.com/api/json/v1'

# Present potential recipee ids
def get_recipe_ids_by_ingredient(ingredient="Chicken"):
    try:
        url = f"{base_url}/{API_KEY}/filter.php?i={ingredient}"
        response = requests.get(url)
        data = response.json()
        if data["meals"] != None:
            recipes = [meal["idMeal"] for meal in data["meals"]]
            return recipes
        else:
            print(f"No recipes with that ingredient")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipe ids by ingredient: {e}", file=sys.stderr)
        return None

# Get basic recipe info by ingredient (optimized - returns name and image too)
def get_recipes_with_basic_info(ingredient="Chicken"):
    try:
        url = f"{base_url}/{API_KEY}/filter.php?i={ingredient}"
        response = requests.get(url)
        data = response.json()
        if data["meals"] != None:
            # Return full meal data including name and image
            recipes = [{
                "id": meal["idMeal"],
                "name": meal["strMeal"],
                "image": meal["strMealThumb"]
            } for meal in data["meals"]]
            return recipes
        else:
            print(f"No recipes with that ingredient")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes by ingredient: {e}", file=sys.stderr)
        return None
    
# Fetch complete details of chosen recipe by ID number
def get_details_by_id(id):
    try:
        url = f"{base_url}/{API_KEY}/lookup.php?i={id}"
        response = requests.get(url)
        return parse_meal_details(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipe details by ID: {e}", file=sys.stderr)
        return None

def parse_meal_details(data):
    meal = data["meals"][0]
    meal_details = {
        "id": meal["idMeal"],
        "name": meal["strMeal"],
        "alternate_name": meal["strMealAlternate"],
        "category": meal["strCategory"],
        "area": meal["strArea"],
        "instructions": meal["strInstructions"],
        "image": meal["strMealThumb"],
        "tags": meal["strTags"],
        "youtube": meal["strYoutube"]
    }
    return meal_details

if __name__ == "__main__":
    print('\n***Get Recipes with Main Ingredient***\n')
    
    ingredient = input('\nPlease provide an ingredient you have in your kitchen: ')

    recipes = get_recipe_ids_by_ingredient(ingredient)

    print("\n")

    if recipes:
        for recipe in recipes:
            pprint(get_details_by_id(recipe))