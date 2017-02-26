** To setup the postgres database:
  (1)start postgres server:
     pg_ctl -D <path to postgers local database > -l logfile start
  (2)create database:
     createdb <db name>
  (3)create user and password
  
 ** Link this postgres database to the Django project
    goto PSVP_project/PSVP_project/setting.py
    change the database setting, put database name, user name, password in.
    
 ** Everytime, models.py is changed, run:
    python3 manage.py migrate
    to migrate the changes to postgres database
    
 ** Every app has it's own views.py, forms.py and models.py,
    but all the urls are in RSVP_project/RSVP_project/urls.py.
    Every templates used by all the apps are saved at :
    RSVP_project/templates
    (not in each app's directory as tutorial)
    
 ** Don't forget to include the app in the installed_app list in setting.py
