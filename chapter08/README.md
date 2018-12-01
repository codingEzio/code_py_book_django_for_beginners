
# Chapter 08 (that's other chapter(s) down below)

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
        - ```./manage.py makemigrations users ```
        - ```./manage.py migrate```

    2. **create a superuser** (must've done the "migrate" first)
    3. now you can go inside the URL```/admin``` now! (unfinished yet)
- but that's not enough actually 
    - one more line! 
    - class CustomUserAdmin on ```admin.py```
    - ```list_display = ['email', 'username', 'age', 'is_staff', ]```
    
    
# Chapter 09 (based on Chapter 08) 

### Home comes the *User Authentication*!
- Okay...

### Wait! Let's creating some templates first :P
- **NEW CONCEPT**
    1. The *Django loader* looks for tmplts in a nested struc ***within each app***.
        - so it means that *if you wanna add templates (specific for the app)*
        - y'll need put it in APP_FOLDER/```templates/APP_FOLDER/TEMPLATES_FILE``` 
    2. Well, I'm just sayin', I won't impl this right away.
    3. (🐶) Here's another quote of author (🐶)
        > ... a project-level ```templates``` folder approach is cleaner & scales better ...
        
### and some templates & UX thoughts
- nothing new about templates
- the page being redirected to after user login successfully, where?
    - normally 'home' (i.e. homepage, sort of)
    - **where's "home" comes from**?
    - right here: PROJECT/APP_FOLDER/```urls.py``` ('name' param)

### Okay, we're gonna write some templates
- first,
    1. ```'DIRS': [os.path.join(BASE_DIR, 'templates')],``` in **settings.py**
    2. two lines in **settings.py** (add to the bottom)
        - ```LOGIN_REDIRECT_URL = 'home'```
        - ```LOGOUT_REDIRECT_URL = 'home'```
- second, the files & folders
    1. proj/*base.html*
    2. proj/*home.html*
    3. proj/*signup.html*
    4. proj/```templates/registration/```*login.html*
- third, related ```urls.py``` & ```views.py```
    - **PROJECT_newspaper_project**/```urls.py```
    - **APP_users/**```urls.py```
- third in details 
    1. proj/urls.py 
        - ```path('users/', include('users.urls')),```
        - ```path('users/', include('django.contrib.auth.urls')),```
        - ```path('', TemplateView.as_view(template_name='home.html'), name='home'),```
    2. app/urls.py
        - ```path("signup/", SignUpView.as_view(), name="signup"),``` (import needed)
    3. app/views.py
        - ```class SignUpView``` (while using the ```forms.py``` we've created before)
- fourth we'll add **one more option** (i.e. *email addr*) in **sign-up page**! 
    - change the two classes: ```CustomUserCreationForm``` & ```CustomUserChangeForm```
        - change both their subclass: ```Meta```
            - change the ```fields``` variable to 
                - ```fields = ('username', 'email', 'age', )```

    
# Chapter 09 (still based on Chapter 08) 

### Add some styles! 
- Here comes the **Bootstrap** !

### Initial setup
- get an "app" (i.e. 'pages') by 
    1. ```./manage.py startapp pages```
    2. add ```'pages.apps.PagesConfig',``` to **settings.py**
- update "urls" (i.e. **urls.py**)
    1. proj/urls.py
    2. app_pages/urls.py
- and then our "views" -> "templates" (kinda a cycle that'll go all along)
- What we're doin' (**FOR NOW**, ONLY **IN THIS CONTEXT** (i.e. 'get an pages app')) is 
    - *replacing the code-gen-homepage* => *templt-html-used-before* 

### bootstrap NOW? 
- *Nah*, let's **write tests first** that for the work we've done for now!!
- Writing them in the ```pages/tests.py```
    - just go check the test file :P 
    - there's new one in contrast to the tests we've written before (i.e. *forms*)

### YES, bootstrap NOW! 
- how we're gonna use it?
    1. dl the files 
    2. name the links (inside .html file)
- We'll firstly update the "base.html".
    - add related links of *css* and *javascript* 
    - it's all added inside (nothing complicated :P)
- 