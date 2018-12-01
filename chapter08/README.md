
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
- ( Most notes were takin as comments (inside ```forms.py``` & ```admin.py```) )
- let django knows it as well 
    1. model class ```CustomUser``` in app/```models.py```
    2. ```AUTH_USER_MODEL = 'users.CustomUser'``` in proj/```settings.py```
- ah! let's create **forms**! 
    - first we'll make two types of *forms*
        1. ```UserCreationForm```
        2. ```UserChangeForm```
- and "registering" them on the ```admin.py```
    - in cmp to before, 
    - now we add a model **and** a *CustomUserAdmin* (addition to default)
- okay! we're ready to go!
    1. ***make some migrations*** first!!! 
        - ```python
./manage.py makemigrations users 
./manage.py migrate
```
    2. **create a superuser** (must've done the "migrate" first)
    3. now you can go inside the URL```/admin``` now! (unfinished yet)