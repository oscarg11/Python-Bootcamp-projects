from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#1.)Have this route say "Hello World"
@app.route('/')
def hello_world():
    return "Hello World!"

#2.)Have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

#3.) Create a url pattern and function that can handle the following examples..
#"Hi Flask!"
#"Hi Michael"
#"Hi John"
#I think I can just use a string variable for this one <name>. (These always default to strings types)
@app.route('/say/<name>')
def hi_name(name):
    return f"Hi {name}!"
#4.) Create one url pattern and function that can handle the following examples...
#Have it say "hello" 35 times
#Have it say "bye" 80 times
#Have it say "dogs" 99 times
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num,word):
    return word * num

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.