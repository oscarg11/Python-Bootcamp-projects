from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models import recipe_model
from flask_app.models import user_model

#create a new recipe
@app.route('/new/recipe')
def recipe_page():
    # route protection
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_recipe.html")

# create a recipe
@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    # post validation
    if not recipe_model.Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    recipe_data={
        "name":request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "date_made":request.form['date_made'],
        "under_30_min":request.form['under_30_min'],
        "user_id":session['user_id']
    }
    print("NEW POST__", request.form)
    recipe_model.Recipe.save_recipe(recipe_data)
    return redirect('/dashboard')

#VIEW RECIPE
@app.route('/recipes/show/<int:id>')
def show_recipe(id):
    # route proetection
    if 'user_id' not in session:
        return redirect('/logout')
    recipe_id ={
        "id": id
    }
    one_recipe = recipe_model.Recipe.get_one_recipe_with_user(recipe_id)
    return render_template("show_recipe.html", one_recipe=one_recipe )

# EDIT Recipe
@app.route("/recipes/edit/<int:id>")
def edit_recipe_form(id):
    # route protection
    if 'user_id' not in session:
        return redirect('/logout')
    recipe_id ={
        "id": id
    }
    one_recipe = recipe_model.Recipe.get_one_recipe_with_user(recipe_id)
    return render_template('edit_recipe.html', one_recipe=one_recipe)

# UPDATE RECIPE
@app.route('/recipes/update/<int:id>', methods=['POST'])
def process_update_recipe(id):
    # post validation
    if not recipe_model.Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    recipe_data={
        "id": id,
        "name":request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "date_made":request.form['date_made'],
        "under_30_min":request.form['under_30_min'],
        "user_id":session['user_id']
    }
    print("UPDATED POST__", request.form)
    recipe_model.Recipe.update_recipe(recipe_data)
    return redirect('/dashboard')
    
# DELETE A RECIPE
@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    recipe_id ={
        "id": id
    }
    print("RECIPE DELETED__", request.form)
    recipe_model.Recipe.delete_recipe(recipe_id)
    return redirect('/dashboard')

