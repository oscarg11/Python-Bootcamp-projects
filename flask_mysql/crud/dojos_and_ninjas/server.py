from flask_app import app
from flask_app.controllers import dojos_routes, ninjas_routes

if __name__=="__main__":
    app.run(debug=True)