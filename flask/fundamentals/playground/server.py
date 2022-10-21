import string
from flask import Flask, render_template
app = Flask(__name__)
# this method uses template index.html to render 3 blue boxes
@app.route('/play')
def play():
    return render_template('index.html', color = "blue", x = 3)

#this method renders x amount of boxes
@app.route('/play/<int:x>')
def playTwo(x):
    return render_template("index.html",x = x, color = "blue")

#This method renders x amount of boxes
#while also changing the color of all boxes
@app.route('/play/<int:x>/<string:color>')
def playThree(x,color):
    return render_template("index.html",x=x, color=color)

if __name__=="__main__":   
    app.run(debug=True) 