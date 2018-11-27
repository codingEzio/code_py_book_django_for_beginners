### (Almost) the same steps
- how? 
    1. ```django-admin startproject msg_board_project .```
    2. ```python3 manage.py startapp posts```
    3. ```python3 manage.py migrate```
    

### Why *migrate*? (the opt itself)
- firstly 
    - **sync** the db with the current state of 
        1. any database **models** contained in the project 
        2. & listed in ```INSTALLED_APPS``` (inside ```settings.py```)