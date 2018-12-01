
### Custom User Model 
- It's just means:
    - in real life, the default option provided is not enough
    - customzing ur own which accomplish 
        - reach ur needs
        - more secure (as it should be)
- Ah, we still need Django, 
    - yet we're gonna use a simpler one: ```AbstractUser```
    

### Initial setup 
- initial 
    1. ```django-admin startproject``` **```newspaper_project```** ```.```
    2. ```python manage.py startapp``` **```users```**
- migrate?
    - not yet, we'll it after we created the ***customized user model***
- base 
    1. let Django "knows" the app: ```'users.apps.UsersConfig'``` (in ```settings.py```)


### Customizing user model
- let django knows it as well 
    1. model class ```CustomUser``` in app/```models.py```
    2. ```AUTH_USER_MODEL = 'users.CustomUser'``` in proj/```settings.py```