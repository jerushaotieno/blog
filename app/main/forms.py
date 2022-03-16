from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, DateField, SelectField,BooleanField,PasswordField
from ..models import User
from wtforms import ValidationError

#Edit profile



class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')            

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


# user subscription

class SubscriberForm(FlaskForm):
    email = StringField('Enter your email address to subscribe to our blog',validators=[DataRequired(),Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('This email is in use')


# new blog post 

class BlogForm(FlaskForm):
    title = StringField('Blog Title ',validators = [DataRequired()])
    description = TextAreaField('Add your blog post ',validators=[DataRequired()])
    # postedby = StringField('Posted By: ',validators = [DataRequired()])
    date = DateField('Posting Date', validators=[DataRequired()])
    submit = SubmitField('Add Blog')


# update blog

class UpdateBlog(FlaskForm):
    description = TextAreaField('Update your blog', validators=[DataRequired()])
    submit = SubmitField('Update blog')


# delete blog post

class DeleteBlog(FlaskForm):
    description = TextAreaField('Are you sure you want to delete this blog?', validators=[DataRequired()])
    submit = SubmitField('Delete blog')


# comments

class CommentForm(FlaskForm):
    comment = TextAreaField('Write your comment here',validators=[DataRequired()])
    # madeby = StringField('Made By: ',validators = [DataRequired()])
    dateposted = DateField('Posting Date', validators=[DataRequired()])
    submit = SubmitField('Add Comment')

