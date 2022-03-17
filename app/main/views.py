from app import app
from flask import render_template,redirect,url_for, abort,request,flash

from app.auth.forms import LoginForm
from . import main
from flask_login import login_required
from ..models import Blog, Comments, Subscribe, User
from .forms import SubscriberForm, UpdateProfile, BlogForm, UpdateBlog
from .. import db
from ..email import mail_message

from app.requests import get_random_quote


@main.route('/', methods = ["GET","POST"])
def index():

    quotes = get_random_quote()

    form = SubscriberForm()
    if form.validate_on_submit():
        subscribe = Subscribe(email = form.email.data)

        db.session.add(subscribe)
        db.session.commit()

        mail_message("Welcome to the Blog Alert community!","email/subscribe",subscribe.email,user=subscribe)

        flash("Subscribed successfully. You'll never run short on inspiration!")

        return redirect (url_for('auth.login'))
        # return redirect(url_for('main.index'))

    blogs = Blog.query.all()

    return render_template('index.html', form = form, quotes=quotes, blogs=blogs)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



# Update profile view function

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


#  upload picture

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         # filename = photos.save(request.files['photo'])
#         # path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))



# blog

@main.route('/blog/', methods = ["GET","POST"])
@login_required
def post():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog = Blog(title=blog_form.title.data, description=blog_form.description.data, author=blog_form.author.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.post'))

    return render_template('blog.html', blog_form= blog_form)


# blog update

@main.route('/updateblog/', methods = ["GET","POST"])
@login_required
def update():
        
    form = UpdateBlog()

    if form.validate_on_submit():
        description = form.description.data

        blog = UpdateBlog(description=description)
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.post'))

    return render_template('updateblog.html',form =form)


# blog delete

@main.route('/deleteblog/', methods = ["GET","POST"])
@login_required
def delete():
        
    form = UpdateBlog()

    if form.validate_on_submit():
        description = form.description.data

        blog = UpdateBlog(description=description)
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.home'))

    return render_template('updateblog.html',form =form)


    


