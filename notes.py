"""
Title:      notes.py
Desc:       notes for the Django Project

github link: https://github.com/bmon1216/django-blog.git
"""

""" Getting started with Django
the first thing we do is pip install django(3.1.5)
this creates additional tools we can use in the terminal
we will be using the django tool: django-admin (use help for a list of tools)
"""

""" How manage.py Works
The `django-admin` command that we used to create the project has 
sub-commands that allow you to:

    creating a new project or app
    running the development server
    executing tests
    entering a python interpreter
    entering a database shell session with your database
    much much more (run django-admin without an argument)

We then need to create a site project, use the command
django-admin startproject <projectname>

This will creates a new directory in our project called the project name

manage.py - used to run the server and do other functions

(second) projectname directory - the project directory, holds the settings for
the project

we can run the server to test it by running 'python manage.py runserver'
"""

""" Creating the database
database settings are defined in project directory -> settings.py under
the DATABASES = {} field

Note: by default, Django databases use SQLite3 and name the db: 'db.sqlite3'

We create the database by running: 'python manage.py migrate'
Create a super user for the db: 'python manage.py createsuperuser'
"""

""" Creating an app
we can create apps now into our database. For example, a polling app:
    'python manage.py startapp polling'
    
This creates a new entry directory 'polling'. We now add the app to our 
settings.py under 'Installed_Apps' 
"""

""" Creating a local Git version

-> CD into the main project directory
-> git init
-> create a new file called '.gitignore'
-> add to the file:
        *.pyc
        *.db
        *.sqlite3
"""

""" Views
We use views (either our own functional views or Django built-in views) to
receive a request and return a response (usually render a template).

Common view tasks are:
    -Retrieving an object from the database and injecting it into a template.
    -Receiving form input from a user, and using that form input to persist 
    an object into the database.
    -Retrieving a collection of objects from the database and injecting 
    them into a template.
"""
