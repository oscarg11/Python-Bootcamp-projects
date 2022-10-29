from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'secret password'
#main form page
@app.route('/')
def index():
    return render_template("index.html")
#Saves user's input in session and redirects it so that it can be rendered on a page.
@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['yourname'] = request.form['name']
    session['dojolocation'] = request.form['location']
    session['language'] = request.form['favlanguage']
    #Only the selected radio button will be displayed
    session['time-option']=request.form['time-options']
    #checkboxes can be retrieved by calling the getlist method
    session['checkedbox'] = request.form.getlist('checkbox')
    session['comment'] = request.form['comment']
    return redirect('/results')
#recieves the user's input to be rendered on a result page.
@app.route('/results')
def results():
    print(request.form)
    return render_template('results.html',name_on_template=session['yourname'],
    location_on_template=session['dojolocation'], language_on_template=session['language'],
    checkbox_on_template=session['checkedbox'], comment_on_template=session['comment'])


if __name__ == "__main__":
    app.run(debug=True)

