from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    blog = db.relationship('Pitches',backref = 'user',lazy = "dynamic")


# for blog

class Blog(db.Model):

    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comments', backref = 'blog', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog(cls, id):
        blog = Blog.query.filter_by(id=id).all()
        return blog

    def __repr__(self):
        return f'User{self.username}'



# for comments

class Comments(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    blog_id = db.Column(db.Integer,db.ForeignKey("blog.id"))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments= Comments.query.filter_by(id=id).all()
        return comments

    def __repr__(self):
        return f'User{self.username}'