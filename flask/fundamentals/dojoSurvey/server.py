from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'secret password'
#main form page
@app.route('/')
def index():
    return render_template("index.html")

#process form input
@app.route('/process', methods=['POST'])
def process_form():
    print("submitted info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favlanguage'] = request.form['favlanguage']
    # Only the selected radio button will be displayed
    session['time_options'] = request.form['time_options']
    # check boxes can be accessed by calling the getList method
    session['checkbox'] = request.form.getlist('checkbox')
    session['comment'] = request.form['comment']

    return redirect('/results')

#redirect to display results page
@app.route('/results')
def display_results():
    print("DISPLAYING USER FORM INFO")
    print(request.form)
    return render_template("results.html", name_on_template=session['name'], location_on_template=session['location'], favlanguage_on_template=session['favlanguage'],
    radio_on_template=session['time_options'],checkbox_on_template=session['checkbox'],comment_on_template=session['comment'])

if __name__ == "__main__":
    app.run(debug=True)

