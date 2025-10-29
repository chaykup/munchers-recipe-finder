from flask import Flask, render_template, request, jsonify
from recipes import get_recipe_ids_by_ingredient, get_details_by_id, get_recipes_with_basic_info
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# API endpoint to get recipe IDs by ingredient
@app.route('/api/recipes/search')
def search_recipes():
    ingredient = (request.args.get('ingredient') or "").strip()
    
    if not ingredient:
        return jsonify({"error": "No ingredient provided"}), 400
    
    # OPTIMIZED: This now makes only ONE API call and returns all data
    recipes_data = get_recipes_with_basic_info(ingredient)
    
    if not recipes_data:
        return jsonify({"error": "No recipes found with that ingredient"}), 404
    
    return jsonify({"recipes": recipes_data})

# API endpoint to get full recipe details by ID
@app.route('/api/recipes/<recipe_id>')
def get_recipe_details(recipe_id):
    details = get_details_by_id(recipe_id)
    
    if not details:
        return jsonify({"error": "Recipe not found"}), 404
    
    return jsonify(details)

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", message="Not Found"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", message="Internal Server Error"), 500

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)