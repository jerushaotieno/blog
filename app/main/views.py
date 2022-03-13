from app import app
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm
from ..models import Review

@app.route('/')

def landing_page():
    return render_template('index.html') 

@app.route('/blog')
def home():
    return render_template('blog.html')