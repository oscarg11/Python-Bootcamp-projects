from flask import Flask, render_template, request, redirect

from flask_app import app
# ...server.py

#import the class from user.py
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    #call the get_all() class method to get all users
    print(users)
    return render_template("read(all).html", users=User.get_all())

#renders the creat a new user page
@app.route('/users/new')
def new_user():
    return render_template('create.html')

#processes the users form input
@app.route('/user/create_user', methods=["POST"])
def create_user():
    print(request.form)
    User.save_user(request.form)
    return redirect('/users')

#route to render the edit form
@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit.html", users=User.get_one(data))

#route to render the show page
@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("show.html", users=User.get_one(data))

#takes in update method 
@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/users')
