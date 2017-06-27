# Scrum Board
Scrum Board made with Django Rest Framework and Angular 1

#### Virtual environment

Creates an isolated environment for installing packages, 
without conflict with other python projects in personal computer.

It's assumed that you ran alias python="python3"

If you use python2, you should use virtualenv package

**More info**: "Python Developer's Toolkit"

- Create virtual environment named djangular 

        python -m venv djangular

- Activate virtual environment (venv) from root folder (./)
        
        source djangular/bin/activate

- Activate venv from virtual environment folder (./djangular/)

        . bin/activate
        
- Exit venv

        deactivate
        
- Install Django (inside djangular folder and with venv activated)

        pip install django
        # to create a project inside venv folder - ./djangular/djangular/
        django-admin.py startproject djangular

- Run the server (inside ./djangular/djangular/)
        
        python manage.py runserver
        
        
        
    
        
        