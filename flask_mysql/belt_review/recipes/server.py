from flask_app.controllers import users_routes
from flask_app.controllers import recipes_routes
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)
# ...server.py