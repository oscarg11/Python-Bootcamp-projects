from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return render_template('index.html')
@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def hello(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output
    

if __name__=="__main__":   
    app.run(debug=True)    

