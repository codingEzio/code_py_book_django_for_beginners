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
- and ..
    1. 