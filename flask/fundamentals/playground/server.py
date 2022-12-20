from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#1.)render three blue boxes 
@app.route('/play')
def three_blue_boxes():
    return render_template('index.html',x=3) #box color is set to blue and x is set to 3 by default

#2.) render x amount of boxes
@app.route('/play/<int:x>')
def x_amount_of_boxes(x):
    return render_template("index.html", x=x)

#3.) render x amount of boxes, and have them in appear in x color
@app.route('/play/<int:x>/<color>')
def x_color(x, color):
    return render_template("index.html", x=x, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.