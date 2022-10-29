
from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)

app.secret_key = 'Secret'
#records the number of times the user has visited the page 
@app.route('/')
def initial_count():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1

    return render_template('index.html', count=session['count'])

#"plustwo" adds two visits while "reset" resets or clears the count to 1
@app.route('/count', methods=['POST'])
def modified_count():
    if request.form['button'] == "plustwo":
        session['count'] += 1
    else:
        session.clear()
    return redirect('/')

#clears the session and redirects back to the root route
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)