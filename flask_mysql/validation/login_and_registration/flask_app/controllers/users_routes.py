from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
# home page
@app.route('/')
def index():
    return render_template('index.html')

# REGISTER A USER: Validates register form input
# and saves user to db then stores into session
@app.route('/register', methods=['POST'])
def register_user():
    if not User.validate(request.form):
        return redirect('/')
    # if valid the form input is saved to the db and user is stored in session!
    print("NEW USER REGISTERED__",request.form)
    session['user_id']= User.save_user(request.form)
    return redirect('/welcome')

# LOGIN_USER(): validates login form input
#  and checks if user's email exist in db
@app.route('/login', methods=['POST'])
def login_user():
    if not User.validate_login(request.form):
        return redirect('/')
    # IF EMAIL EXISTS THE USER IS LOGGED IN & STORED IN
    print("USER HAS LOGGED IN__",request.form)
    one_user=User.get_by_email(request.form)
    session['user_id']= one_user.id
    return redirect('/welcome')

#WELCOME() CHECKS IF USER IS IN SESSION (logged in)
# ONLY ALLOWS LOGGED IN USERS ACCESS TO WELCOME PAGE
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        "id": session['user_id']
    }
    return render_template('welcome.html', user=User.get_one_user(data))

#LOGOUT(): "logs out" and clears session
@app.route('/logout')
def logout():
    print("USER HAS LOGGED OUT")
    session.clear()
    return redirect('/')