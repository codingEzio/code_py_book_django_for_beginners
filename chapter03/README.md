
### (almost) the same step
- ***note***: down below may not the actual steps 
    - it might be the exec order rather the impl order.
- how? (along with new concept)
    1. init project && init app 
    2. make a folder (root/templates/XX.html)
    3. project/settings.py: [new-app, template-folder]
    4. project/urls (point to app)
        1. app/urls.py 
        2. app/views.py 
        3. using the template (3->2->1, actually)

### the 'url' patterns
- ***note***: 1st param is regex, the name is the difinite one.
- start with ```https://LINK/``` 
- param 'name' were accessed by ```?home```

### template! 
- where 
    - root folder (same level as 'project' (or 'app'))
- about the ```base.html```
    - content of ```block content``` could be overwritten by its child
- syntax 
    - ```{% ... %}```

### writing tests 
- let's start 
    - write ```tests.py``` inside the app folder 
        - using ```SimpleTestCase``` instead as we're not using a db
    - run tests (project folder)
        - ```python manage.py test```

<hr>

### Go production! 
- steps 
    - get [*heroku*](https://heroku.com) working
        1. installing cli: ```brew install heroku/brew/heroku```
        2. ```heroku autocomplete``` (*brew*'s instruction)
        3. add two files 
            - ```pip freeze >``` ***requirements.txt***
            - **web: gunicorn PROJECTNAME.wsgi --log-file -** in ```Procfile``` (specifically for **Heroku**)
        4. installed related module
            - ```pip install gunicorn==19.9.0``` (it IS the latest version, btw)
        5. changing ```settings.py```: ```ALLOWED_HOSTS = ['*']```
    - do *heroku* related things 
        1. ***note***: it might takes **LOTS OF** time, or try to access a page (which resolved that issue!)
        2. ```HEROKU_DEBUG=true HEROKU_DEBUG_HEADERS=1 heroku login -i``` 
        3. ```sudo heroku create```
        4. what I get 
            - https://afternoon-earth-27926.herokuapp.com/
            - https://git.heroku.com/afternoon-earth-27926.git
    - and some little extra work
        - add *git hooks* 
            - ```sudo heroku git:remote -a afternoon-earth-27926``` (the name came from lines above!)
        - static-files optimizing? no! (not yet)
            - ```sudo heroku config:set DISABLE_COLLECTSTATIC=1```
    - IT JUST NOT BLOODY WORK :) 
        - one last step (cannot ```push``` successfully)
        - (note: the rest of steps will be added later)