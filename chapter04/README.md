### (Almost) the same steps 
- initial steps 
    1. ```django-admin startproject msg_board_project .```
    2. ```python3 manage.py startapp posts```
    3. ```python3 manage.py migrate```
    

### Why *migrate*? (the opt itself)
- firstly 
    - **sync** the db with the current state of 
        1. any database **models** contained in the project 
        2. & listed in ```INSTALLED_APPS``` (inside ```settings.py```)


### let's write some *models*
- firstly 
    - go ```app_folder/models.py```
    - then do these two steps 
        1. ```python manage.py makemigrations``` **```APP_NAME```**
        2. ```python manage.py migrate``` **```APP_NAME```**
- something to **notice**
    - what did it do?
        1. *generate* more detailed ```model``` code (by Django, of course)
        2. actually making changes to DB (e.g. **db.sqlite3**)
    - ya can *omit* the 'APP_NAME' (e.g. ```posts```)
        - but ***don't***, just DON'T
        - do make it as **small** and **isolated** as possible! :P

- **Superuser**!
    - concept (beginning)
        - ```models.py``` -> *make migrations* -> ```admin.py```
        - the actual steps were (while I was learning :P)
            1. ```models.py```
            2. *make migrations*
            3. get a user ```python manage.py createsuperuser``` 
            4. register the **app** (i.e. ```Posts```) at the ```admin.py```
    - about the ```models.py```
        - it could also affect the *view* side (sort of)
            - e.g. add a ```__str__``` (part-of-content as Title)