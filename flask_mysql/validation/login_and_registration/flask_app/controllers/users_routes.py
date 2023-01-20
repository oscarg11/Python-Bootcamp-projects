from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
# home page
@app.route('/')
def index():
    return render_template('index.html')

# Register a user
@app.route('/register', methods=['POST'])
def register_user():
    #(VALIDATION)if form input not valid it redirects back form page
    if not User.validate(request.form):
        return redirect('/')
    # if valid the form input is saved/inserted to the db
    print("NEW USER REGISTERED__",request.form)
    User.save_user(request.form)
    return redirect('/welcome')

# login
@app.route('/login', methods=['POST'])
def login_user():
    if not User.validate_login(request.form):
        return redirect('/')
    #store user in session
    user_email={
        "email":request.form['email']
    }
    one_user=User.get_by_email(user_email)
    session['user_id']= one_user.id
    return redirect('/welcome')

#welcome page
@app.route('/welcome')
def welcome():
    # if user is not logged in redirect back to home
    if 'user_id' not in session:
        return redirect('/logout')
    user_id={
        "id": session['user_id']
    }
    return render_template('welcome.html', user=User.get_one_user(user_id))

#logout method: "logs out" and clears session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')