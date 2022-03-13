# Author

Jerusha Otieno

# Description

This is a python/flask personal blogging website allowing the writer to create and share their opinions with users. The writer can sign into the blog, create a new blog post, delete insulting/degrading user comments, and to update and delete blogs created. Users can view blog posts on the site, comment on them, view the most recent blogs and view random qquotes on the site. The users also get an email alert when a new post is made by joining a subscription. 

# Live Link

View Site: 

# User Story

The writer can:
* Sign in to the blog
* Create a blog from the application
* Delete insulting or degrading comments
* Update and delete blogs created

The blog user can:
* View the blog posts on the site
* Comment on blog posts
* View the most recent posts
* Get an email alert when a new post is made by joining a subscription
* See random quotes on the site

# BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | On page load | Get all posts; Select between signup and login
| Select SignUp	| Email, Username & Password	| Redirect to login
| Select Login	| Username & password | Redirect to page with blog posts 
| Select comment button	| Comment | Form that you input your comment
| Click on submit |  | Redirect to all comments template with your comment & other comments

# Development Installation

To get the code:

1. Clone the Repository

https://github.com/jerushaotieno/blog.git

2. Move to the folder and install requirements

cd blog 
pip install -r requirements.txt

3. Export Configurations

export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

4. Run the application
python3 manage.py server

5. Test the application
python3 manage.py test

6. Open the application on your browser 127.0.0.1:5000.

# Technology Used

* Python3.8
* Flask
* Heroku
* Bootstrap

# Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

# Contact Information

If you have any question or contributions, please email: jerushaotienocoding@gmail.com 

# License

MIT License:

# Copyright 

Copyright (c) 2022 Jerusha Otieno 