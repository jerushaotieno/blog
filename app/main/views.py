from app import app
from flask import render_template,redirect,url_for, abort,request

from app.auth.forms import LoginForm
from . import main
from flask_login import login_required
from ..models import Comments, User
from .forms import UpdateProfile
from .. import db,photos



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home/')
def home():
    login = LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(email = login.email.data).first()
        if user is not None and user.verify_password(login.password.data):
            user(user,login.remember.data)
            return redirect(request.args.get('next') or url_for('main.homepage'))

    return render_template('home.html',login=login)

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


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))