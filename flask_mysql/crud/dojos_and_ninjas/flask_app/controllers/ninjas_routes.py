from flask_app import app
# ...server.py
from flask_app.models import dojo, ninja
from flask import render_template,redirect, request

# Renders the new ninja form 
@app.route('/ninja')
def new_ninja_form():
    print("ADD NEW NINJA",request.form)
    return render_template("new_ninjas.html", dojo_options=dojo.Dojo.get_all_dojos())

# add a new ninja from form input
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    print("NEW NINJA CREATED")
    ninja.Ninja.save_ninja(request.form)
    return redirect('/dojos')

# edit ninja & call the get_a_ninja() method to target a row by id
@app.route('/ninjas/edit/<int:id>')
def edit_ninja(id):
    data = {
        "id":id
    }
    return render_template('update_ninja.html', ninjas=ninja.Ninja.get_a_ninja(data))

# returns updated data to db
@app.route('/update_ninja', methods=['POST'])
def update_ninja():
    ninja.Ninja.update_ninja(request.form)
    return redirect('/')

#delete
@app.route('/ninja/delete/<int:id>')
def delete_ninja(id):
    data ={
        "id":id
    }
    ninja.Ninja.delete_ninja(data)
    return redirect('/')


