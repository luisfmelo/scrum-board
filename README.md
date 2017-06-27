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

- Start a new app (we need to add it to ./djangular/djangular/djangular/settings.py - INSTALLED APPS)

        python manage.py startapp scrumboard

- Migrations

        python manage.py makemigrations
				python manage.py migrate 

- Admin Panel - if I want to manage tables in admin panel, i need to add them in admin.py

        python manage.py createsuperuser 

- Django Rest Framework
	1. Install via pip 
				pip install djangorestframework
	2. In settings.py, add 'rest_framework' to INSTALLED APPS
	3. Add Serializers (to encode JSON): Create a file/folder: serializers
	4. REST Api Views: Create file api.py with the Controllers (Views in Django) that push info from db and serialize it
  5. URLS
	  5.1. create scrumboard/urls.py with the urlpatterns (regex expression) and the View (controller) it will call (.asView())
    5.2. add in djangular/urls.py a sub endoint that includes the previous created file
