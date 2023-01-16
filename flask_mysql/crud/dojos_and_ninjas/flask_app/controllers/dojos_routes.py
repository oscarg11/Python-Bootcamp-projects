from flask_app import app
from flask_app.models.dojo import Dojo
from flask import redirect, render_template, request

# root route will redirect to dojos home page (view dojos)
@app.route('/')
def index():
    return redirect('/dojos')

#render dojos home page template
@app.route('/dojos')
def dojos():
    return render_template("dojos.html", all_dojos = Dojo.get_all_dojos())

#add a new dojo to the db from form input
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save_dojo(request.form)
    return redirect('/dojos')

#displays a single dojo's info
@app.route('/dojos/show/<int:id>')
def show_dojo(id):
    print("DISPLAY DOJO'S NINJAS",request.form)
    data = {
        "id":id
    }
    return render_template("show_dojo.html",display_dojo=Dojo.get_dojos_with_ninjas(data))
