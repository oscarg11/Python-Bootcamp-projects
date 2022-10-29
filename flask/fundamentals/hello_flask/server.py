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

@app.route('/template/<string:banana>/<int:num>')
def template(banana,num):
    return render_template("hello.html",banana=banana, num=num)

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


if __name__=="__main__":   
    app.run(debug=True)    

