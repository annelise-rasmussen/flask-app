from flask import Flask, render_template
from markupsafe import Markup
from recipes import recipes

app = Flask(__name__)

@app.route('/')
def home():
    titleText = "Gluten Free Baking/Cooking Favs!"
    bodyText = Markup("""
        <br>
        <h1>We love all things Gluten Free here</h1>
        <nav>
        <ul>
            <li><a href="/Baking" class="button-link">Baking</a></li>
            <li><a href="/Cooking" class="button-link">Cooking</a></li>
        </ul>
        </nav>
    """)
    return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/Baking')
def baking():
    titleText = "Favorite Baking Websites"
    bodyText = Markup("""
        <br>
        <h1>Here are a few websites I get most of my recipes from:</h1>
        <br>
	<br>
	<ul>
            <li><a href="https://theloopywhisk.com/" target="_blank">The Loopy Whisk</a></li>
            <li><a href="https://www.mamaknowsglutenfree.com/" target="_blank">Mama Knows Gluten Free</a></li>
            <li><a href="https://meaningfuleats.com/" target="_blank">Meaningful Eats</a></li>
        </ul>
    """)
    return render_template('template.html', titleText=titleText, bodyText=bodyText)
@app.route('/Cooking')
def cooking():
    titleText = "Favorite Cooking Recipes"
    bodyText = Markup("""
	<br><br><br>
	<h1>Favorite Cooking Recipes:</h1>
        <ul>
	<li><a href="/recipe/baked-oatmeal">Baked Oatmeal</a></li>
	<li><a href="/recipe/blueberry-baked-oatmeal">Blueberry Baked Oatmeal</a></li>
	<li><a href="/recipe/breakfast-casserole">Breakfast Casserole</a></li>
	<li><a href="/recipe/pancakes">Pancakes</a></li>
	<li><a href="/recipe/baked-atlantic-salmon">Baked Atlantic Salmon</a></li>
	<li><a href="/recipe/bbq-pizza">BBQ Pizza</a></li>
	<li><a href="/recipe/beef-stew">Beef Stew</a></li>
	<li><a href="/recipe/breaded-chicken">Breaded Chicken</a></li>
	<li><a href="/recipe/crockpot-bbq-chicken">Crockpot BBQ Chicken</a></li>
	<li><a href="/recipe/fresh-salsa">Fresh Salsa</a></li>
	<li><a href="/recipe/guacamole">Guacamole</a></li>
	<li><a href="/recipe/indian-butter-curry">Indian Butter Curry</a></li>
	<li><a href="/recipe/mediterranean-bowl">Mediterranean Bowl</a></li>
	<li><a href="/recipe/roasted-veggies">Roasted Veggies</a></li>
	<li><a href="/recipe/southwest-chicken-cutlet">Southwest Chicken Cutlet</a></li>
	<li><a href="/recipe/smokey-bacon-chili">Smokey Bacon Chili</a></li>
	</ul>
    """)
    return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/recipe/<recipe_name>')
def show_recipe(recipe_name):
    recipe = recipes.get(recipe_name)
    if recipe:
        return render_template('recipe.html', titleText=recipe["title"], ingredients=recipe["ingredients"], instructions=recipe["instructions"])
    else:
        return "Recipe not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
