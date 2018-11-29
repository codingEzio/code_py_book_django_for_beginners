### steps (initial phase)
- okay 
    1. project & app 
    2. let Django know the new app: ```blog.apps.BlogConfig```
- then 
    1. add what we need to ```blog/models.py```
    2. generate detailed *models* 
        1. ```./manage.py makemigrations``` **blog**
        2. ```./manage.py migrate``` **blog**
    3. create an admin ```./manage.py createsuperuser```
    4. register the app in ```blog/admin.py``` (should be done early!!)
- and the routines (urls, views etc.)
    - urls 
        - proj level, app level
    - views
        - related: model, template 
            - template: PROJ/templates
                1. base.html
                2. home.html 


### new thing: **static files**
- initial 
    - make A DIR (proj level) e.g. 
        - proj
        - proj/static
        - proj/static/css
        - proj/static/css/***base.css**
- really add some styles 
    1. static folder created (& files of course) 
    2. let Django *knows* where it is (declare in ```settings.py```
        - type ```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]``` 
    3. load it into template
        - at top: ```load static```
        - header: ```<link href="{% static 'css/base.css' %}" rel="stylesheet">```