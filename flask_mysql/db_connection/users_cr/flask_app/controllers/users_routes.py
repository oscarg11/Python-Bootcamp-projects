from flask import render_template, request, redirect # Import Flask to allow us to create our app
from flask_app.models.user import User #import User class

from flask_app import app

#root route
@app.route('/')
def index():
    return redirect('/users')

#call the get_all() method from users.py to display all users in db
@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)


@app.route('/users/new')
def render_create_page():
    return render_template("create.html")

#process form data & save it to db
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

# calls the get_one() method to target a specific user by id
@app.route('/users/show/<int:id>')
def show_user(id):
    print(request.form)
    data = {
        "id":id
    }
    return render_template("show.html", show_user=User.get_one(data))

# update user & call the get_one() method to target a row by id
@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {
        "id":id
    }
    return render_template('update_user.html', user_id=User.get_one(data))

# returns updated data to db
@app.route('/update_user', methods=['POST'])
def update_user():
    User.update(request.form)
    return redirect('/')

#delete
@app.route('/users/delete/<int:id>')
def delete_user(id):
    data ={
        "id":id
    }
    User.delete(data)
    return redirect('/')