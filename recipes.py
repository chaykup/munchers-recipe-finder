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

    # Get recipes with basic info (id, name, image)
    recipes = get_recipes_with_basic_info(ingredient)

    if recipes:
        print("\n--- Available Recipes ---\n")
        # Display recipes in JSON-like format with id and name
        for recipe in recipes:
            print(f"ID: {recipe['id']} - {recipe['name']}")
        
        print("\n")
        
        # Prompt user to select a recipe ID
        recipe_id = input("Enter the recipe ID to see full details (or press Enter to exit): ").strip()
        
        if recipe_id:
            # Get and display full details for selected recipe
            details = get_details_by_id(recipe_id)
            if details:
                print("\n--- Recipe Details ---\n")
                pprint(details)
            else:
                print(f"\nError: Could not find recipe with ID {recipe_id}")
        else:
            print("\nExiting...")
    else:
        print(f"\nNo recipes found with ingredient: {ingredient}")