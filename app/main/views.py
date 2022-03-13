from app import app
from flask import render_template,request,redirect,url_for
from . import main


@main.route('/')

def landing_page():
    return render_template('index.html') 

@main.route('/blog')
def home():
    return render_template('blog.html')