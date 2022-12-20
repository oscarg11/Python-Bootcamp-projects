
from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)

app.secret_key = 'Secret'
#records the number of times the user has visited the page 
@app.route('/')
def index():
    if 'count' not in session:
        session['count']=1
    else:
        session['count']+=1
    return render_template("index.html",count = session['count'])

#Ninja Bonus: Add a +2 button underneath the counter and a new
#route that will increment the counter by 2.
#Ninja Bonus: Add a reset button to the reset the counter.
@app.route('/counter',methods=['POST'])
def manipulate_count():
    if request.form['button'] == "plustwo":
        session['count']+=1
    else:
        session.clear()
    return redirect('/')

#destroys session: clears the session and redirects to the route rout to test it
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)