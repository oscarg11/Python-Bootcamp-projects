from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
# from flask_app.models.recipe_model import Recipe

#LOGIN REGISTER PAGE
@app.route('/')
def index():
    return render_template('index.html')

#DASHBOARD CHECKS IF USER IS IN SESSION (logged in)
# ONLY ALLOWS LOGGED IN USERS ACCESS TO WELCOME PAGE
@app.route('/dashboard')
def welcome():
    # route protection
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        "id": session['user_id']
    }
    # display users with recipes
    get_all_recipes = Recipe.get_all_recipes_with_creator()
    return render_template('dashboard.html', current_user=User.get_one_user(data), all_recipes = get_all_recipes)

# REGISTER A USER: Validates register form input
# and saves user to db then stores into session
@app.route('/register', methods=['POST'])
def register_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    # if valid the form input is saved to the db and user is stored in session!
    print("NEW USER REGISTERED__",request.form)
    session['user_id']= User.save_user(request.form)
    return redirect('/dashboard')

# LOGIN_USER: validates login form input
@app.route('/login', methods=['POST'])
def login_user():
    if not User.validate_login(request.form):
        return redirect('/')
    # if email exists then the user is logged and stored in session
    print("USER HAS LOGGED IN__",request.form)
    one_user=User.get_by_email(request.form)
    session['user_id']= one_user.id
    return redirect('/dashboard')

#LOGOUT(): "logs out" and clears session
@app.route('/logout')
def logout():
    print("USER HAS LOGGED OUT")
    session.clear()
    return redirect('/')