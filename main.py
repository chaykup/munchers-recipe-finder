from flask import Flask, render_template, request
from recipes import get_recipe_ids_by_ingredient, get_details_by_id
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recipes')
def get_recipe():
    ingredient = (request.args.get('ingredient') or "").strip()
    recipes = get_recipe_ids_by_ingredient(ingredient)
    details = get_details_by_id(recipes[0])
    return render_template(
        "recipes.html",
        name = details['name'],
        image = details['image'],
        instructions = details['instructions']
    )

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", message="Not Found"), 404

@app.errorhandler(500)
def not_found(e):
    return render_template("error.html", message="Not Found"), 500

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)