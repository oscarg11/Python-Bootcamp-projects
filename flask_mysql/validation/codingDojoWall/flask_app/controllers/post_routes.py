from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models import post_model
from flask_app.models import user_model


# create a post
@app.route('/create_post', methods=['POST'])
def createPost():
    # post validation
    if not post_model.Post.validation_post(request.form):
        return redirect('/wall')
    post_data={
        "content":request.form['content'],
        "user_id":session['user_id']
    }
    post_model.Post.save_post(post_data)
    return redirect('/wall')

# delete post(only logged in users can delete their own post)
@app.route('/delete/<post_id>')
def delete_post(post_id):
    post_model.Post.delete_post(post_id)
    return redirect('/wall')
