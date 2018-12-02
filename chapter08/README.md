
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

    
# Chapter 10 (still based on Chapter 08) 

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
- so ... we've *"imported"* the files (```.css```, ```.js```)
    - now we could apply any styles to the elements 
        - (specifically other than the **base.html**)
    - e.g. we changed the button style of **login.html**
        - ```<button class="btn btn-success ml-2" type='submit'>Log In</button>```

### Let's talk about the **sign-up** page :P
- (specifically the 'password requirement' (or sayin' "help_text"), stylish concerns I assume)
- We're not tring to 'replace' (or sayin' "overwrite") the "help_text", 
    - instead, we're using a third-party modules named ***django-crispy-forms***
        - install it by ```pip3 install django-crispy-forms==1.7.2``` (the ver. is optional)
    - then let Django "knows" it by (**settings.py**)
        1. INSTALLED_APPS -> add ```'crispy_forms',``` 
        2. at the bottom -> add ```CRISPY_TEMPLATE_PACK = 'bootstrap4'``` 
- we can use it for our templates! (steps of modifying ```signup.html```)
    1. load it by ```{% load crispy_forms_tags %}``` (right after the ```extends```)
    2. changes 
        - before: ```{{ form.as_p }}```
        - after: ```{{ form | crispy  }}```

    
# Chapter 11 (still based on Chapter 08) 

### Now, we're gonna talk about "password change & reset" 
- "We" will mention both 
    1. the **built-in** 
    2. and **our-customized-version** (powered by Bootstrap) (plus *email service*)

### how you get there (ver: built-in)
- type URL/```users/password_change``` (it works, just to be clear)

### customize our own **password change**
- firstly, templates! 
    1. proj/```templates/registration/```**```password_change_form.html```**
    2. proj/```templates/registration/```**```password_change_done.html```**
- once u've written them, just refresh the page, it's done! 

### lastly, let's talk about the **password reset**
- quotes from author (*a reminder for myself*) (slightly changed a few words)
    1. ... *the steps (i.e. "reset") are similar to conf password change* ...
    2. ... *Django already provides a default impl that we'll use and then customize* ...

### we'll use the Djangos' first (**settings.py**)
- the basic usage
    1. add ```EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'``` to the bottom
    2. go to [Password reset](http://localhost:8000/users/password_reset/)
    3. typing the email addr which was used while registering (you might don't have it XD)
    4. check the terminal (e.g. ```runserver```)
    5. there should be an email sent from *Django* itself  
        - access the url it provided 
        - typing the new passwd, then it's all done 
    6. some notes here
        - ya always should provided ur email while registering (debug purposes!)
        - *Django* will NOT mistaken whose password will be changed (even there's an user was online (by cookie))
- and might add some styles, shall we?
    - four templates, please! 
        1. ```templates/registration/```**```password_reset_form.html```**
        2. ```templates/registration/```**```password_reset_done.html```**
        3. ```templates/registration/```**```password_reset_confirm.html```**
        4. ```templates/registration/```**```password_reset_complete.html```**
    - its exec orders (in users' perspective) 
        - form => access the reset url (type ur email)
        - done => notification (we've sent for ya)
        - confirm => typing new password (**link** provided by Django (**at terminal**))
        - complete => reset complete (still notification)


# Chapter 12 (still based on Chapter 08) 

### Emails! 
- Third-party service: [SendGrid](https://sendgrid.com/)

