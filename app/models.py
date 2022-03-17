from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager



# for role

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


# for user

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    blog = db.relationship('Blog',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You can only read this attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User{self.username}'





# for blog

class Blog(db.Model):

    __tablename__ = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(2000))
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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# subscribers

class Subscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    email = db.Column(db.String(255),unique = True,index = True)


    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    

    @classmethod
    def get_subscriber(cls, id):
        subscriber= Subscribe.query.filter_by(id=id).all()
        return subscriber

    def __repr__(self):
        return f'User {self.name}'


# random quotes

class Quotes:
    def __init__(self,author,quote):
        self.author = author
        self.quote =  quote