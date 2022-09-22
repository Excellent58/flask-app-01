from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Post
from . import db

def get_post(post_id):
    post = Post.query.get(post_id)
    return post

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts) 

@views.route("/python-posts")
def python():
    posts = Post.query.filter_by(_category='python')
    return render_template("py.html", posts=posts)

@views.route("/javascript")
def javascript():
    posts = Post.query.filter_by(_category='javascript')
    return render_template("js.html", posts=posts)

@views.route("/posts")
def posts():
    post_id = request.args.get('post_id')
    post = get_post(post_id)
    return render_template("view-post.html", post=post)

@views.route("/admin")
def admin():
    posts = Post.query.all()
    return render_template("admin.html", posts=posts)

@views.route("/create-post", methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        post_title = request.form.get('post_title')
        _category = request.form.get('_category')
        description = request.form.get('description')
        text = request.form.get('text')


        if not post_title and _category and description and text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(post_title=post_title, _category=_category, description=description, text=text)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_post.html')

@views.route("/edit", methods=('GET', 'POST'))
def edit():
    post_id = request.args.get('post_id')
    post = get_post(post_id)

    if request.method == 'POST':
        post_title = request.form['post_title']
        description = request.form['description']
        _category = request.form['_category'] 
        text = request.form['text']

        if not post_title:
            flash('title is required')
        else:
            post.post_title = post_title
            post.description = description
            post._category = _category
            post.text = text
            db.session.commit()
            print(post.text)
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template('edit.html', post=post)

@views.route("/<int:id>/delete", methods=(['POST']))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('views.home'))