from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Blogs',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read this attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User{self.username}'















#  class Quotes:
#     '''
#     Quote class to define Quote Objects
#     '''

#     all_quotes = []

#     def __init__(self,id, quote, author, permalink):
#         self.id =id
#         self.quote = quote
#         self.author = author
#         self.permalink = "http://quotes.stormconsultancy.co.uk/quotes/"

#     def save_quote(self):
#         Quote.all_quoteseviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,id):

#         response = []

#         for review in cls.all_reviews:
#             if review.movie_id == id:
#                 response.append(review)

#         return response