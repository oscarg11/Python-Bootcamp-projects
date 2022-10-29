from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def boardOne():
    return render_template('index.html',x=8,y=8)

@app.route('/<int:y>')
def boardTwo(y):
    return render_template('index.html',x=8,y=4)

@app.route('/<int:x>/<int:y>')
def boardThree(x,y):
    return render_template('index.html',x=x, y=y)

# @app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
# def changeColor(x,y,color1,color2):
#     return render_template('index.html',x=x,y=y,color1=color1,color2=color2)




if __name__=="__main__":
    app.run(debug=True)