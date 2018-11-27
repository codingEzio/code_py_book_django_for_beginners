
### Cheatsheet

- **django-admin**
    - create a project 
        - ```startproject heyworld .```


- **python manage.py**
    - create an app
        - ```startapp APP_NAME```
    - run server 
        - ```runserver```

### *app* structure
- admin, app 
    - both are conf file 
    - BIT-Django-admin-app, app-itself
- migrations/
    - changes of ```models.py``` ( db <-> model.py ) KEEP-IN-SYNC
- models
    - define db models (Django trans it into db tables)
- views
    - handle the req/resp logic 

### when u add an app
- *declare* it in ```PROJECT/settings.py```
- add an ```urls.py``` if it doesn't exist 

### view & urlconf 
- mechanics
    - what to display 
    - where that content is going (i.e. addr)
- procedure 
    1. app/views
    2. app/urls (use ```import```)
    3. PROJECT/urls (use ```include``` of Django)
- about the **urlpatterns**'s ```path()``` in **urls.py** 
    1. PATH  (e.g. "" means '/')
    2. views.homepage  (correspond to ```views.py```)
    3. name="home"  (it's ?optional) (access by ***URL/?name***)

### temp-notes 
- newapp: 
    - -> setting -> app-folder 
    - -> proj_url -> app_url -> app_view -> model (& db)

### conventions 
- I found the ```urlpatterns``` in ```urls.py``` is ?required by *Django*
    - which means you can NOT change it to anythin' else 