from flask import Flask, render_template, request, redirect # Import Flask to allow us to create our app
from users import User #import User class
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

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
def render_form_page():
    return render_template("create.html")

#process form data
@app.route('/create_user', methods=["POST"])
def create_friend():
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



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
